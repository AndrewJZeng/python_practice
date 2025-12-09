#version 330 core
struct Light {
    vec3 position;
  
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
};

uniform Light light;

uniform float shininess;

uniform vec3 viewPos;

out vec4 FragColor;

in vec3 FragPos;
in vec3 Normal;
in vec2 TexCoords;

uniform sampler2D texture_diffuse1;

void main()
{
    vec3 outNorm = -Normal;
    //set amount of levels for cell shading
    float diffLevels = 4.0;
    float specLevels = 2.0;
    float specTexBlend = 0.1; //var for how much tex color comes through in spec
    
    vec4 texColor = texture(texture_diffuse1, TexCoords);
    
    // ambient
    vec3 ambient = light.ambient * texColor.rgb;
      
    // diffuse
    vec3 norm = normalize(outNorm);
    vec3 lightDir = normalize(light.position - FragPos);
    float diff = max(dot(norm, lightDir), 0.0);
//    float cellShaded = floor(diff * diffLevels) / diffLevels;
    float cellShaded = 0.0;
    if (diff < 0.4) cellShaded = 0.0;
    else if (diff < 0.6) cellShaded = 0.5;
    else cellShaded = 1.0;
    vec3 diffuse = light.diffuse * (cellShaded * texColor.rgb);
    
    // specular
    vec3 viewDir = normalize(viewPos - FragPos);
    vec3 reflectDir = reflect(-lightDir, norm);
    float specLevel = max(dot(viewDir, reflectDir), 0.0); //calcs direction
    float cellSpec = 0.0;//ceil(specLevel * specLevels) / specLevels;
    if (specLevel < 0.99) cellSpec = 0.0;
    else cellSpec = 1.0;
    float spec = pow(cellSpec, shininess); //calcs shininess
    vec3 specular = light.specular * (spec); //* texColor.rgb
        
    vec3 result = ambient + diffuse + specular;
//    if (Normal == vec3(0.0, 0.0, 0.0)) FragColor = vec4(1.0, 0.0, 0.0, 1.0);
//    else FragColor = vec4(0.0, 1.0, 0.0, 1.0);
//    FragColor = vec4(norm.xyz, 1.0);
    FragColor = vec4(result, 1.0);
}
