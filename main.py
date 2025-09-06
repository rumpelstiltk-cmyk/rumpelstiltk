from flask import Flask, render_template, request

app = Flask(__name__)

strategies = {
    "워런 버핏": "장기 가치 투자, 안정적인 기업 위주",
    "일론 머스크": "하이리스크, 하이리턴 혁신 테마 투자",
    "피터 린치": "잘 아는 기업에 집중 투자"
}

@app.route("/", methods=["GET", "POST"])
def index():
    selected_strategy = None
    if request.method == "POST":
        investor = request.form.get("investor")
        selected_strategy = strategies.get(investor, "전략이 없습니다.")
    return render_template("index.html", strategies=strategies, selected_strategy=selected_strategy)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    # 업비트 비트코인 시세 조회 예시
    url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC"
    response = requests.get(url)
    data = response.json()
    
    btc_price = data[0]['trade_price'] if data else None
    
    # 포트폴리오 데이터 예시
    portfolio = {
        "Bitcoin": 0.05,   # 보유 수량
        "Ethereum": 0.5
    }
    
    # 총 자산 계산
    total_value = 0
    if btc_price:
        total_value += portfolio["Bitcoin"] * btc_price
    # Ethereum 시세는 0으로 예시 (추후 API 추가 가능)
    
    return render_template("index.html", btc_price=btc_price, total_value=total_value, portfolio=portfolio)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
btc_price = None
try:
    url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC"
    response = requests.get(url)
    data = response.json()
    btc_price = data[0]['trade_price'] if data else None
except Exception as e:
    print("업비트 API 오류:", e)
