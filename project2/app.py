#app.pyの中のルーティングにかかる部分をreview.pyに分離する

from flask import Flask

app = Flask(__name__)

# ここまででオッケー

# importでreview.pyを読み込む
import review

if __name__ == "__main__":
    # use a different port if 5000 is already in use
    app.run(debug=True, port=5100)
    