#version 330 core
struct Material {
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
    float shininess;
};
  
uniform Material material;

struct Light {
    vec3 position;
  
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
};

uniform Light light;

out vec4 FragColor;

in vec3 Normal;
in vec3 FragPos;

uniform vec3 viewPos;

void main()
{
    //set amount of levels for cell shading
    float levels = 2.0f;
    // ambient
    vec3 ambient = light.ambient * material.ambient;
      
    // diffuse
    vec3 norm = normalize(Normal);
    vec3 lightDir = normalize(light.position - FragPos);
    float diff = max(dot(norm, lightDir), 0.0);
    float cellShaded = floor(diff * levels) / levels;
    vec3 diffuse = light.diffuse * (cellShaded * material.diffuse);
    
    // specular
    vec3 viewDir = normalize(viewPos - FragPos);
    vec3 reflectDir = reflect(-lightDir, norm);
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), material.shininess);
    vec3 specular = light.specular * (spec * material.specular);
        
    vec3 result = ambient + diffuse + specular;
//    FragColor = vec4(Normal * 0.5 + 0.5, 1.0);
//    FragColor = vec4(vec3(gl_FragCoord.z), 1.0);
    FragColor = vec4(result, 1.0);
}
