from camel.agents.deductive_reasoner_agent import DeductiveReasonerAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType

print(f"------------------------------------")

m1_model = ModelFactory.create(
	model_platform=ModelPlatformType.OLLAMA,
	model_type="llama3.2:3b",
    url="http://localhost:11434/v1", #optional
	model_config_dict={"temperature":0.4},
)

# Initialize the agent with the model (optional, default model can be used if not provided)
agent = DeductiveReasonerAgent(model=m1_model)

# Define the starting state of a project
starting_state = "The project has just started. The team has been formed, and the project goals have been outlined. However, the project has not yet started any major tasks."

# Define the target state of the project
target_state = "The project has reached its first milestone. The first task has been completed on time, and the team is ahead of schedule."

# Define optional roles involved in the reasoning
role_descriptions = {
    "ProjectManager": "Responsible for overseeing the project and ensuring deadlines are met.",
    "TeamMember": "Responsible for completing specific tasks and reporting progress."
}

deduction_result = agent.deduce_conditions_and_quality(
    starting_state=starting_state,
    target_state=target_state,
    role_descriptions_dict=role_descriptions
)

response = agent.step("Get this done")

if hasattr(response, 'msgs') and response.msgs:
    msg_content = response.msgs[0].content
    
    # Extract conditions
    conditions = []
    if "Logical Deduction of Conditions" in msg_content:
        conditions_section = msg_content.split("Logical Deduction of Conditions")[1].split("Entity/Label Recognition")[0]
        condition_lines = [line.strip() for line in conditions_section.split("condition") if ":" in line]
        for line in condition_lines:
            parts = line.split(":", 1)
            if len(parts) > 1:
                conditions.append(parts[1].strip())
    
    # Extract quality assessment
    quality = "No quality assessment available."
    if "Quality Assessment" in msg_content:
        quality_section = msg_content.split("Quality Assessment")[1].split("Iterative Evaluation")[0]
        quality_text = quality_section.replace("($Q$) (do not use symbols):", "").strip()
        quality = quality_text
    
    # Print results
    print("Extracted Conditions:")
    for condition in conditions:
        print(f"- {condition}")
    print("\nExtracted Quality Assessment:")
    print(quality)




# for i, msg in enumerate(object1):
#     print(f"Message {i+1}:")
#     print(msg.content)
#     print("-" * 50)

# # for condition in deduction_result.get("conditions", []):
# #     print(f"- {condition}")

# for i, msg in enumerate(object1.msgs):
#     print(f"Message {i+1}:")
#     print(msg.content)
#     print("-" * 50)