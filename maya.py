import os
import openai as op

class Maya:
    def __init__(self):
        self.__client = op.OpenAI(api_key=os.getenv('MAYA_KEY'))
        self.__model = 'ft:gpt-3.5-turbo-1106:personal::8Vt3dKaQ'
        self.__res = self.__client.chat.completions.create(
            model=self.__model,
            messages=[
                {'role': 'system', 'content': r"You are a professional sexologist and from now on your name will be Maya. Your knowledge of sex therapy is based on professional sex therapists such as Marty Klein or like Otis Milburn from the Netflix series 'Sex Education'. Your therapy is aimed at teenagers aged 15 and over (schoolchildren, students, etc.). You will give a UNIQUE advice and UNIQUE recommendations on sex therapy, relationships and solving questions from users. Your answers shouldn't be repetitive, they should always be unique to each query (even repeated ones) and relevant. You \"listen\" to the user and adapt to him create a comfortable atmosphere for them in communication. Sometimes you will remind them that you are just an AI, and if something really bothers a person, then it is better to contact a professional and there is nothing wrong with that. You will give answers in UKRAINIAN language."}
            ]
        )
        self.__messages = [{'role': self.__res.choices[0].message.role,
                            'content': self.__res.choices[0].message.content}]

    def send_message_and_get_content(self, message: str, role: str='user') -> str:
        self.__messages.append({'role': role, 'content': message})
        res = self.__client.chat.completions.create(model=self.__model,
                                                    messages=self.__messages)
        self.__messages.append({'role': res.choices[0].message.role,
                                'content': res.choices[0].message.content})

        return res.choices[0].message.content