import random
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, LocationSendMessage,SourceUser
)


app = Flask(__name__)

line_bot_api = LineBotApi('nK0voUnJfwLaei+dOiUs05iXBtsslx6S+ULExMxWfh8G2H8Ez2JDM/5p39Zo+gg0BL48FZ+Qb8H0F/GuYZ8lrbjM2NtcFwpVidPivTjezyUkqm7d8POyFcwL58l6rGHbD+o8VUN0nNSwff7JqjaPVQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b231dbdec4dfdcbe65b7c6afadce90af')

	
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
	
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
	
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
	
# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
    # line_bot_api.reply_message(
        # event.reply_token,
        # TextSendMessage(text=event.message.text))
	

# global m
# m = 0
# global a
# a = 0

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	text = event.message.text
	if text == "男一宿":
		L = ['仙桃', '自助餐', '陽光早餐', '全家', '喜樂早餐','滷味','心情客飯']
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(L[random.randint(0,6)])			
		)
	if text == "男二宿":
		L = ['A華', '嵐媽', '饌堡', '莎慕達', '山口','美而美','怡園餐廳']
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(L[random.randint(0,6)])			
		)			
		
	

if __name__ == "__main__":
    app.run()