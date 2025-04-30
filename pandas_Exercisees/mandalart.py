import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform

# 한글 폰트 설정 (운영체제별로 자동 설정)
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin':  # macOS
    plt.rc('font', family='AppleGothic')
else:
    plt.rc('font', family='DejaVu Sans')  # 리눅스 등

plt.rcParams['axes.unicode_minus'] = False

# 9칸 구성 (3x3)
texts = [
    "[건강]\n필라테스 시작\n테니스 루틴\n건강한 식단",
    "[유튜브]\n10만 목표\n일상+레시피 콘텐츠\n댓글 소통",
    "[내면 성장]\n감정 흘려보내기\n시크릿 실천\n마음의 평화",
    "[인간관계]\n진짜 친구\n소소한 추억\n진심의 교류",
    "🌟 나는 내 삶을\n스스로 창조하며 살아가는\n단단하고 따뜻한 여성이다 🌟",
    "[직장]\n3월 합격\n워라밸 팀\n성장 기회",
    "[장기 기반]\n노후 안정\n한국 귀국 준비\n재정적 자립",
    "[비자/이민]\n안정적 비자\n이민 설계\n자유로운 이동",
    "[주거]\n햇살 가득\n예쁜 공간\n나만의 평화"
]

# 그리기
fig, ax = plt.subplots(figsize=(10, 10))
ax.axis("off")

# 격자와 텍스트 출력
for i in range(3):
    for j in range(3):
        idx = i * 3 + j
        ax.text(j + 0.5, 2.5 - i, texts[idx], va='center', ha='center',
                bbox=dict(boxstyle="round,pad=0.5", fc="#f0f8ff", ec="black"),
                fontsize=11)

# 격자 선
for i in range(4):
    ax.plot([0, 3], [i, i], color='black', linewidth=1)
    ax.plot([i, i], [0, 3], color='black', linewidth=1)

plt.xlim(0, 3)
plt.ylim(0, 3)
plt.tight_layout()
plt.savefig("my_mandalart.png", dpi=300)
plt.show()