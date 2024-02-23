def compare_project_prompt(my_project: str, existing_project: str) -> list[dict[str, str]]:
    # Instruction for the GPT system role: setting the context for the task with a personal touch.
    info_sys = {
        "role": "system",
        "content": ("As an assistant to an academic researcher, your task is to analyze a provided "
                    "project description and compare it with the researcher's project idea. "
                    "Evaluate their relevance, similarities, and differences to assist in understanding "
                    "how the existing project aligns with the researcher's objectives. "
                    "Please use 'your' to directly address the researcher in a personalized manner.")
    }

    # User prompt: Detailed questions and formatting instructions for the response, emphasizing personalization.
    info_user = {
        "role": "user",
        "content": f'''#### Begin Questions ####
        Q1: Provide a one-sentence summary of the existing project.
        Q2: Identify and describe similarities between this existing project and your idea.
        Q3: Enumerate the differences between the existing project and your idea.
        Q4: Assign a similarity score from 0 to 100, indicating the degree of relevance between the two projects:
           - 0-20: Not relevant (Different fields, no shared methodologies)
           - 20-40: Somewhat relevant (Same subfield, some shared aspects)
           - 40-60: Relevant (Similar problems or methodologies, citation worthy)
           - 60-80: Very relevant (Similar problems and methodologies)
           - 80-100: Extremely relevant (Nearly identical problems and methodologies)
           Ensure the score is a precise number within this range.
        Q5: Justify the assigned score with a brief explanation, referring to "your project" to maintain personalization.
        #### End Questions ####

        #### Begin Instructions ####
        Format your response as a JSON object with the following structure:
        {{
            "Summary": "A concise summary of the existing project.",
          "Similarity": "Detailed similarities between the projects, referring to 'your project'.",
          "Difference": "Key differences noted, again referring to 'your project'.",
          "Score": "The similarity score, as a numerical value.",
          "Reason": "Explanation for the assigned score, ensuring to address the user personally."
        }}
        Use the exact keys provided above for your response and maintain a personalized tone throughout.
        #### End Instructions ####

        #### Begin Input ####
        Existing project information: [{existing_project}].
        Your project description: [{my_project}].
        #### End Input ####
        '''
    }
    return [info_sys, info_user]
