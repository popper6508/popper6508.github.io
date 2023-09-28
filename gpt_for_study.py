import openai

def generate_chapter(topic, num_chapter, to_who):
    system_message_01 = """I will give you specific format \n
                           input \n
                           ----------- \n
                           (Economics, 5, Entrepreneur) \n
                           ------------ \n
                           this means "'Economics 'textbook for 'entrepreneur' composed of '5' Chapter" \n

                           Then, assume you as  text book maker, make "'Economics 'textbook optimized to 'entrepreneur' composed of '5' Chapter" in this example with ordering \n

                           NOTE THAT | Don't add any comment. I will directly use it as prompt to other chat! Also, don't say 'I'm just AI model not analyst...'
                           
                           your output format

                           ------------ \n

                           1. ~~~~
                           2. ~~~~
                           ......
                           n. ~~~
                           """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message_01},
            {"role": "user", "content": f"({topic}, {num_chapter}, {to_who})"}
        ],
        max_tokens=100 * num_chapter
    )

    text = response.choices[0].message.content.strip()
    chapters = text.split('\n')[:num_chapter]
    return chapters


def generate_outline(chapters, to_who):
    outlines = []
    for i in range(len(chapters)):
        system_message_02 = """I'll give you input, then you have to follow the output type

                               user input type: (Chapter name, For Whom such as graduate students)

                               your output type
                               -------------- 
                               1. ~~~~
                                 - 
                               2. ~~~~
                                 - 
                               ......
                               n. ~~~
                                 -

                               NOTE: Don't attach any additional replies such as "for whom... understanding....", except outline. I will directly use it as an outline for other chat prompts! Please strictly follow the instructions.
                            """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message_02},
                {"role": "user", "content": f"({chapters[i]}, {to_who})"}
            ],
            max_tokens=1000
        )
        outline = response.choices[0].message.content.strip()
        outlines.append(outline)
    return outlines


def generate_handbook(outlines):
    books = []
    for i in range(len(outlines)):
        system_message_03 = """1. I'll give you an outline,
                              then you must write a full chapter, which means writing the entire book and not just filling in the outline.
                           2. Don't reply with anything except the result of the writing.
                              NOTE: Don't attach any additional replies such as "for whom... understanding...." or "Here's the writing". I will directly use the content!
                           3. It's better not to include 'Report', 'Chapter', 'Introduction', or 'Conclusion'.
                           Please strictly follow the instructions.
                            """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message_03},
                {"role": "user", "content": outlines[i]}
            ],
            max_tokens=1000
        )
        writing = response.choices[0].message.content.strip()
        books.append(writing)
    return books


def gpt_for_book(topic, num, for_whom):
    chapters = generate_chapter(topic, num, for_whom)
    outlines = generate_outline(chapters, for_whom)
    books = generate_handbook(outlines)
    return chapters, books
