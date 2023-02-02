import openai
import telebot

openai.api_key = "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"
bot = telebot.TeleBot("6123793991:AAEiNCpsTmiY1Rsdj7Wi4wE862i1V6OT5jc")

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    if message.chat.type == "supergroup":
        if "draw" or "нарисуй" in message.text.lower():
            response = openai.Image.create(
                prompt=message.text,
                n=1,
                size="1024x1024"
            )
            image_url = response['data'][0]['url']
            bot.send_message(chat_id=message.chat.id, text=str(image_url))
        elif "бот" or "bot" or "bot," or "бот," in message.text.lower():
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=message.text,
                temperature=0.0,
                max_tokens=2200,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            )
            bot.send_message(chat_id=message.chat.id, text=response['choices'][0]['text'])
        elif "код." or "code." in message.text.lower():
            response = openai.Completion.create(
                model="text-davinci-002",
                prompt=message.text,
                temperature=0.0,
                max_tokens=2200,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            )
            bot.send_message(chat_id=message.chat.id, text=response['choices'][0]['text'])
        else:
            pass
    else:
        if "draw" or "нарисуй" or "нарисуй," in message.text.lower():
            response = openai.Image.create(
                prompt=message.text,
                n=1,
                size="1024x1024"
            )
            image_url = response['data'][0]['url']
            bot.send_message(chat_id=message.from_user.id, text=str(image_url))
        elif "бот" or "bot" or "bot," or "бот," in message.text.lower():
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=message.text,
                temperature=0.0,
                max_tokens=2200,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            )
            bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])
        elif "код." or "code." in message.text.lower():
            response = openai.Completion.create(
                model="text-davinci-002",
                prompt=message.text,
                temperature=0.0,
                max_tokens=2200,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            )
            bot.send_message(chat_id=message.chat.id, text=response['choices'][0]['text'])

bot.polling()

#условия страт слова
#для нейросетки photorealistic 4k nikon
#залить на сервер
#кнопки, инлайн

#def menu():
  #  print("Welcome to the chatbot!")
  #  print("Please choose one of the following options:")
  #  print("1. Option 1")
  #  print("2. Option 2")
  #  choice = input("Enter your choice: ")
  #  if choice == "1":
  #      option1()
  #  else:
   #     print("Invalid choice. Please try again.")
   #     menu()

  #  def option1():
  #  text = input("Enter your text: ")
   # print("You entered: " + text)
#
  #  def option2():
 #   text = input("Enter your text: ")
 #   print("You entered: " + text)
#
 #   menu()