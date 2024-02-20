def compare_project_prompt(my_project: str, existing_project: str) -> list[dict[str, str]]:

    info_sys = {
        "role": "system",
        "content": "You are an academic researcher's assistant, I want to you read a project description and tell me how it is relevant to my idea."
    }

    info_user = {
        "role": "user",
        "content": f'''####Begin Questions####
        Q1: Write a one-sentence summary of the input project.
        Q2: What are the similarities between this project and my idea?
        Q3: What are the differences between the project and my idea?
        Q4: Please provide a similarity score from 0 to 100, where a higher score indicates greater relevance between two projects. Use the following calibration for the scores:
        0-20: Not relevant; Projects from different fields with no shared methodologies or insights, e.g., one project on natural language processing and the other on computer graphics.
        20-40: Somewhat relevant; Projects from the same subfield, such as adversarial learning, neural rendering, or tangible input interfaces.
        40-60: Relevant; Projects addressing similar problems (e.g., increasing the robustness of adversarial learning, tangible input interfaces in AR), or using similar methodologies to solve different problems. Projects with this level of similarity should be considered for citation.
        60-80: Very relevant; Projects addressing similar problems and using similar techniques.
        80-100: Mostly relevant; Projects addressing almost identical problems and using similar techniques.
        Make sure the score is a number between 0 and 100 e.g., 81, 23, 45, 90, 98...
        Q5: Please briefly state the reason for your score.
        ####End Questions####
        ####Begin Instructions####
        Please provide your answer in .json format. The keys are <Summary>, <Similarity>, <Difference>, <Score>, <Reason>.
        <Summary> is a one-sentence summary of the input paper (Q1).
        <Similarity> is the similarities between this paper and my idea (Q2).
        <Difference> is the differences between the paper and my idea (Q3).
        <Score> is the similarity score (Q4).
        <Reason> is the reason for your score (Q5).
        ####End Instructions####
        ####Begin Input####
        This is the information of a project I found: [{existing_project}].
        This is the description of my idea: [{my_project}].
        ####End Input####
        '''
    }
    return [info_sys, info_user]
