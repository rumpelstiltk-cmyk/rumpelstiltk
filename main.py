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
