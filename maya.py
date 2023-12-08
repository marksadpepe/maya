import os
import openai as op

class Maya:
    def __init__(self):
        self.__client = op.OpenAI(api_key=os.getenv('MAYA_KEY'))
        self.__res = self.__client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'system', 'content': r"You are a professional sex therapist and from now on your name will be Maya. your knowledge in sex therapy is based on real people's knowledge, as well as on the knowledge of characters Jean Milburn (a practicing sexologist) and Otis Milburn from Netflix's 'Sex Education'. You will give advice and recommendations on sex therapy and relationship matters, as well as constantly remind that you are an artificial intelligence and can not 100% give advice, and that it is better to consult a doctor with such questions."}
            ]
        )
        self.__messages = [{'role': self.__res.choices[0].message.role,
                            'content': self.__res.choices[0].message.content}]

    def send_message_and_get_content(self, message: str, role: str='user') -> str:
        self.__messages.append({'role': role, 'content': message})
        res = self.__client.chat.completions.create(model='gpt-3.5-turbo', messages=self.__messages)
        self.__messages.append({'role': res.choices[0].message.role,
                                'content': res.choices[0].message.content})

        return res.choices[0].message.content