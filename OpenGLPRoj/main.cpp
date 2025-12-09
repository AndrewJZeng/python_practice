#include <glad/glad.h>
#include <GLFW/glfw3.h>

#include "stb_image.h"
#include "headers/shader_s.h"
#include "headers/camera.h"
#include "headers/model.h"
#include "headers/primitive.h"

#include <iostream>
#include <cmath>

#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>

#include <imgui.h>
#include <imgui_impl_glfw.h>
#include <imgui_impl_opengl3.h>

void framebuffer_size_callback(GLFWwindow* window, int width, int height);
void processInput(GLFWwindow *window);

//mouse movement
void mouse_callback(GLFWwindow* window, double xpos, double ypos);
void scroll_callback(GLFWwindow* window, double xoffset, double yoffset);


//camera funcs
void mouse_callback(GLFWwindow* window, double xpos, double ypos);
void scroll_callback(GLFWwindow* window, double xoffset, double yoffset);

// settings
const unsigned int SCR_WIDTH = 800;
const unsigned int SCR_HEIGHT = 600;

int dimx = 256;
int dimy = 256;

//set up vars for camera
Camera camera(glm::vec3(0.0f, 0.0f, 3.0f));

//set up vars for mouse movement and cam rotation
bool firstMouse = true;
float lastX = SCR_WIDTH / 2.0f;
float lastY = SCR_HEIGHT / 2.0f;

//set up vars for tracking deltaTime
float deltaTime = 0.0f; //this is time between current frame and last frame
float lastFrame = 0.0f;

//vars to edit through imgui
static float translation[] = {0.0, 0.0, 0.0};
static float rotation[] = {0.0, 0.0, 0.0};
static float lightAmbient[] = {0.2, 0.2, 0.2};
static float lightDiffuse[] = {1.0, 1.0, 1.0};
//static float lightSpec[] = {0.0, 0.0, 0.0};

static float matAmbient[] = {1.0, 0.5, 0.31};
static float matDiffuse[] = {1.0, 0.5, 0.31};
static float matShininess = 1.0f;

int textSize = 2048;
static char *vtext = new char[textSize];
static char *ftext = new char[textSize];

//get position in worldspace for lightsource
glm::vec3 lightPos(1.2f, 1.0f, 2.0f);
glm::vec3 modelPos(0.0f, -5.0f, 0.0f);
glm::vec3 cubeScale(5.0f, 5.0f, 5.0f);

glm::vec3 manScale(0.3f, 0.3f, 0.3f);
glm::vec3 manPos(0.0f, 5.0f, -5.0f);

//glm::vec3 cubePos(-3.0f, 0.0f, -3.0f);
//glm::vec3 floorPos(0.0, -2.0f, -5.0f);

void drawIMGUI(Shader* ourShader) {
    // Show a simple window that we create ourselves. We use a Begin/End pair to created a named window.
    {
        // Start the Dear ImGui frame
        ImGui_ImplOpenGL3_NewFrame();
        ImGui_ImplGlfw_NewFrame();
        ImGui::NewFrame();

//        static float f = 0.0f;

        ImGui::Begin("Graphics For Games");  // Create a window and append into it.

        ImGui::Text("Application average %.3f ms/frame (%.1f FPS)", 1000.0f / ImGui::GetIO().Framerate, ImGui::GetIO().Framerate);
        
        //set up sliders on the window
        ImGui::SliderFloat3("position", translation, -10.0, 10.0);
        ImGui::SliderFloat3("rotation", rotation, 0.0, AI_MATH_PI * 2);

        // lighting sliders
        ImGui::SliderFloat3("Ambient lighting", lightAmbient, 0.0, 1.0);
        ImGui::SliderFloat3("Diffuse lighting", lightDiffuse, 0.0, 1.0);
        
        //material sliders
        ImGui::SliderFloat3("Material ambient lighting", matAmbient, 0.0, 1.0);
        ImGui::SliderFloat3("Material diffuse lighting", matDiffuse, 0.0, 1.0);
        ImGui::SliderFloat("Material shininess", &matShininess, 0.0, 32.0);
        
//        bool offScreen;
//        ImGui::Checkbox("Use Offscreen Buffer", &offScreen);

        
        static ImGuiInputTextFlags flags = ImGuiInputTextFlags_AllowTabInput;
        
        ImGui::InputTextMultiline("Vertex Shader", vtext, textSize, ImVec2(-FLT_MIN, ImGui::GetTextLineHeight() * 16), flags);
    
        ImGui::InputTextMultiline("Fragment Shader", ftext, textSize, ImVec2(-FLT_MIN, ImGui::GetTextLineHeight() * 16), flags);

        if (ImGui::Button("Use Shaders", ImVec2(100, 20)))
            ourShader->reload(vtext, ftext);
        
        ImGui::End();

        // IMGUI Rendering
        ImGui::Render();
        ImGui_ImplOpenGL3_RenderDrawData(ImGui::GetDrawData());
    }
}

int main()
{
    // glfw: initialize and configure
    // ------------------------------
    const char* glsl_version = "#version 150";
    
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

#ifdef __APPLE__
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
#endif

    // glfw window creation
    // --------------------
    GLFWwindow* window = glfwCreateWindow(SCR_WIDTH, SCR_HEIGHT, "LearnOpenGL", NULL, NULL);
    if (window == NULL)
    {
        std::cout << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);
    glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);
    
    //tell glfw to get mouse input and call func when mouse moved
    glfwSetCursorPosCallback(window, mouse_callback);
    glfwSetScrollCallback(window, scroll_callback);
                                                  
    //tell glfw to capture mouse cursor
//    glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED);

    // glad: load all OpenGL function pointers
    // ---------------------------------------
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
    {
        std::cout << "Failed to initialize GLAD" << std::endl;
        return -1;
    }
    
    stbi_set_flip_vertically_on_load(true);
    
    IMGUI_CHECKVERSION();
    ImGui::CreateContext();
    ImGui::StyleColorsDark();

    // Setup Platform/Renderer backends
    ImGui_ImplGlfw_InitForOpenGL(window, true);
    ImGui_ImplOpenGL3_Init(glsl_version);
    
    //set default vals for depth and stencil test
    glEnable(GL_DEPTH_TEST);
    glDepthFunc(GL_LESS);

    // build and compile our shader zprogram
    // ------------------------------------
    Shader ourShader("/Users/andrewzeng/dev/OpenGLStuff/OpenGLPRoj/OpenGLPRoj/shaders/basicShader.vs", "/Users/andrewzeng/dev/OpenGLStuff/OpenGLPRoj/OpenGLPRoj/shaders/basicShader.fs");
    
    Shader ourInverted("/Users/andrewzeng/dev/OpenGLStuff/OpenGLPRoj/OpenGLPRoj/shaders/basicShader.vs", "/Users/andrewzeng/dev/OpenGLStuff/OpenGLPRoj/OpenGLPRoj/shaders/basicInverted.fs");
    
    Shader cubeShader("/Users/andrewzeng/dev/OpenGLStuff/OpenGLPRoj/OpenGLPRoj/shaders/3.3.shader.vs", "/Users/andrewzeng/dev/OpenGLStuff/OpenGLPRoj/OpenGLPRoj/shaders/3.3.shader.fs");
    
    Shader outlineShader("/Users/andrewzeng/dev/OpenGLStuff/OpenGLPRoj/OpenGLPRoj/shaders/3.3.shader.vs", "/Users/andrewzeng/dev/OpenGLStuff/OpenGLPRoj/OpenGLPRoj/shaders/outline.fs");
    
    Shader lightShader("/Users/andrewzeng/dev/OpenGLStuff/OpenGLPRoj/OpenGLPRoj/shaders/3.3.shader.vs", "/Users/andrewzeng/dev/OpenGLStuff/OpenGLPRoj/OpenGLPRoj/shaders/lightSourceShader.fs");
    
    //create model
    Model ourModel("/Users/andrewzeng/dev/OpenGLStuff/OpenGLPRoj/OpenGLPRoj/Castle Courtyard/Castle Courtyard.obj");
    
    Model manModel("/Users/andrewzeng/dev/OpenGLStuff/OpenGLPRoj/OpenGLPRoj/Wonder Of U/Wonder Of U.pmx");

    Primitive lightCube("cube", true);
    
    Primitive floorPlane("plane", false);

    float fallSpeed = -1.0f;
    
    //initialize position of model
    ourShader.use();
    manModel.SetModelTranslation(manPos[0], manPos[1], manPos[2]);
    manModel.SetModelScale(manScale[0]);
    
    // render loop
    // -----------
    while (!glfwWindowShouldClose(window))
    {
        // per-frame time logic
        // --------------------
        float currentFrame = static_cast<float>(glfwGetTime());
        deltaTime = currentFrame - lastFrame;
        lastFrame = currentFrame;
        
        // input
        // -----
        processInput(window);

        // render
        // ------
//        glClearColor(0.1f, 0.1f, 0.1f, 1.0f);
        glClearColor(1.0f, 1.0f, 1.0f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); //clear color and depth buffer every frame
        
        // bind textures on corresponding texture units
//        glBindTexture(GL_TEXTURE_2D, texture);
        
        //set default draw mode
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
        
        //set up shader vals
        ourShader.use();
        //set light source vals
        ourShader.setVec3fv("light.ambient",  glm::vec3(lightAmbient[0], lightAmbient[1], lightAmbient[2]));
        ourShader.setVec3fv("light.diffuse",  glm::vec3(lightDiffuse[0], lightDiffuse[1], lightDiffuse[2])); // darken diffuse light a bit
        ourShader.setVec3fv("light.specular", glm::vec3(1.0f, 1.0f, 1.0f));
        ourShader.setVec3fv("light.position", lightPos);
//
//        //set material properties
//        ourShader.setVec3fv("objectColor", glm::vec3(1.0f, 1.0f, 1.0f));
        ourShader.setVec3fv("material.ambient", glm::vec3(matAmbient[0], matAmbient[1], matAmbient[2]));
        ourShader.setVec3fv("material.diffuse", glm::vec3(matDiffuse[0], matDiffuse[1], matDiffuse[2]));
        ourShader.setVec3fv("material.specular", glm::vec3(0.5f, 0.5f, 0.5f));
        ourShader.setFloat("shininess", matShininess);
        
        //set camera position relative to obj
        ourShader.setVec3fv("viewPos", camera.Position);
        
        //create transformation matrices
        glm::mat4 modelOrigin = glm::mat4(1.0f);
        glm::mat4 view = glm::mat4(1.0f);
        glm::mat4 projection = glm::mat4(1.0f); //initialize as identity matrix
        
        //before rendering, set projection matrix for perspective warping and pass to shader
        projection = glm::perspective(glm::radians(camera.Zoom), (float)SCR_WIDTH / (float)SCR_HEIGHT, 0.1f, 100.0f); //create perspective matrix with 45 deg fov, aspect ratio width/height, with front plane 0.1f near and 100f far clipping planes
        
        //create view matrix to adjust coords for camera view
        view = camera.GetViewMatrix(); //find lookat matrix by getting the x, y, z axis coming out from camera, then mult by the camera's position to get adjustment needed to accomodate for camera view
        
        //set up projection matrices
        ourShader.setMat4fv("projection", projection);
        ourShader.setMat4fv("view", view);
        
        //copy all vals to inverted shader
        ourInverted.use();
        //set light source vals
        ourInverted.setVec3fv("light.ambient",  glm::vec3(lightAmbient[0], lightAmbient[1], lightAmbient[2]));
        ourInverted.setVec3fv("light.diffuse",  glm::vec3(lightDiffuse[0], lightDiffuse[1], lightDiffuse[2])); // darken diffuse light a bit
        ourInverted.setVec3fv("light.specular", glm::vec3(1.0f, 1.0f, 1.0f));
        ourInverted.setVec3fv("light.position", lightPos);
//
//        //set material properties
//        ourShader.setVec3fv("objectColor", glm::vec3(1.0f, 1.0f, 1.0f));
        ourInverted.setVec3fv("material.ambient", glm::vec3(matAmbient[0], matAmbient[1], matAmbient[2]));
        ourInverted.setVec3fv("material.diffuse", glm::vec3(matDiffuse[0], matDiffuse[1], matDiffuse[2]));
        ourInverted.setVec3fv("material.specular", glm::vec3(0.5f, 0.5f, 0.5f));
        ourInverted.setFloat("shininess", matShininess);
        
        //set camera position relative to obj
        ourInverted.setVec3fv("viewPos", camera.Position);
        //set up projection matrices
        ourInverted.setMat4fv("projection", projection);
        ourInverted.setMat4fv("view", view);
        
        //set up transformation default vals
        modelOrigin = glm::translate(modelOrigin, modelPos);
        
        //set shader vals to outline shader
        outlineShader.use();
        outlineShader.setMat4fv("projection", projection);
        outlineShader.setMat4fv("view", view);
        
        //draw lightsource obj too
        lightShader.use();
        lightShader.setMat4fv("projection", projection);
        lightShader.setMat4fv("view", view);
        
        //draw the cube for lightsource
        lightCube.SetCubeTranslation(lightPos[0], lightPos[1], lightPos[2]);
        lightCube.SetCubeScale(0.2f);
        lightCube.Draw(lightShader, glm::mat4(1.0f));
        
        //set positions of objects
        ourInverted.use();
        ourModel.SetModelTranslation(modelPos[0], modelPos[1], modelPos[2]);
        ourModel.SetModelScale(cubeScale[0]);
        
        manModel.SetModelScale(manScale[0]);
        manModel.ChangeModelTranslation(0.0f, fallSpeed * deltaTime, 0.0f);
        
        //draw outlines
        //for outline, only want to draw the back faces, so enable face-culling
        glEnable(GL_CULL_FACE);
        glCullFace(GL_FRONT);
        glFrontFace(GL_CCW);
        glEnable(GL_LINE_SMOOTH);
        
        //turn on wireframe mode
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
        glLineWidth(1000.0f);
        
        outlineShader.use();
        //draw our model
        manModel.Draw(outlineShader, modelOrigin);
        glFrontFace(GL_CW);
        ourModel.Draw(outlineShader, modelOrigin);
        glFrontFace(GL_CCW);
        
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
        
        //draw front faces of actual objects
        glCullFace(GL_BACK);
        ourShader.use();
//        send transformations to shader
        //draw our model
        manModel.Draw(ourShader, modelOrigin);
        
        //draw background
        ourInverted.use();
        glFrontFace(GL_CW);
        ourModel.Draw(ourInverted, modelOrigin);
        
        //once drawn, disable face-culling again
        glDisable(GL_CULL_FACE);
        glDisable(GL_LINE_SMOOTH);
        
//        printf("%f, %f, %f", camera.Position.x, camera.Position.y, camera.Position.z);
        
        //draw the imgui window
//        drawIMGUI(&ourShader);

        // glfw: swap buffers and poll IO events (keys pressed/released, mouse moved etc.)
        // -------------------------------------------------------------------------------
        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    // optional: de-allocate all resources once they've outlived their purpose:
    // ------------------------------------------------------------------------

    // glfw: terminate, clearing all previously allocated GLFW resources.
    // ------------------------------------------------------------------
    glfwTerminate();
    return 0;
}

// process all input: query GLFW whether relevant keys are pressed/released this frame and react accordingly
// ---------------------------------------------------------------------------------------------------------
void processInput(GLFWwindow *window)
{
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
        glfwSetWindowShouldClose(window, true);

    if (glfwGetKey(window, GLFW_KEY_W) == GLFW_PRESS)
        camera.ProcessKeyboard(FORWARD, deltaTime);
    if (glfwGetKey(window, GLFW_KEY_S) == GLFW_PRESS)
        camera.ProcessKeyboard(BACKWARD, deltaTime);
    if (glfwGetKey(window, GLFW_KEY_A) == GLFW_PRESS)
        camera.ProcessKeyboard(LEFT, deltaTime);
    if (glfwGetKey(window, GLFW_KEY_D) == GLFW_PRESS)
        camera.ProcessKeyboard(RIGHT, deltaTime);
}

// glfw: whenever the window size changed (by OS or user resize) this callback function executes
// ---------------------------------------------------------------------------------------------
void framebuffer_size_callback(GLFWwindow* window, int width, int height)
{
    // make sure the viewport matches the new window dimensions; note that width and
    // height will be significantly larger than specified on retina displays.
    glViewport(0, 0, width, height);
}

// glfw: whenever the mouse moves, this callback is called
// -------------------------------------------------------
void mouse_callback(GLFWwindow* window, double xposIn, double yposIn)
{
    float xpos = static_cast<float>(xposIn);
    float ypos = static_cast<float>(yposIn);

    if (firstMouse)
    {
        lastX = xpos;
        lastY = ypos;
        firstMouse = false;
    }

    float xoffset = xpos - lastX;
    float yoffset = lastY - ypos; // reversed since y-coordinates go from bottom to top

    lastX = xpos;
    lastY = ypos;

    camera.ProcessMouseMovement(xoffset, yoffset);
}

// glfw: whenever the mouse scroll wheel scrolls, this callback is called
// ----------------------------------------------------------------------
void scroll_callback(GLFWwindow* window, double xoffset, double yoffset)
{
    camera.ProcessMouseScroll(static_cast<float>(yoffset));
}

