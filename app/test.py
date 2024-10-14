from functions.answer import answer

answer = answer(
    chat_input = {
        "user_message": "Please make a QR code for the following URL: sell_anything.com",
        "files": ["a.pdf", "cooking_show.mp4", "c.pdf", "b.pdf", "spiderman.mp4"],
        "history": []
    },
)
print(answer.content)