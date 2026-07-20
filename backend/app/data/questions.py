from models.question import Question, ResponseOption

QUESTIONS = [
    Question(
        id=1,
        text="How long do you expect to live in this home?",
        category="Length of Stay",
        responses=[
            ResponseOption(
                id=1,
                text="Less than 2 years",
                weight=-3,
                explanation="Buying has significant upfront costs, making renting the more cost-effective choice for short stays.",
            ),
            ResponseOption(
                id=2,
                text="2 to 5 years",
                weight=-1,
                explanation="A relatively short stay makes it harder to recover the costs of buying.",
            ),
            ResponseOption(
                id=3,
                text="5 to 10 years",
                weight=1,
                explanation="A medium-term stay may justify buying, depending on your overall financial situation.",
            ),
            ResponseOption(
                id=4,
                text="More than 10 years",
                weight=3,
                explanation="A long stay gives you more time to build equity and benefit from home ownership.",
            ),
        ],
    ),
    Question(
        id=2,
        text="How stable is your current income?",
        category="Income Stability",
        responses=[
            ResponseOption(
                id=1,
                text="Very unstable",
                weight=-3,
                explanation="Unstable income makes long-term mortgage repayments more difficult.",
            ),
            ResponseOption(
                id=2,
                text="Somewhat unstable",
                weight=-1,
                explanation="Some income uncertainty increases the financial risk of buying.",
            ),
            ResponseOption(
                id=3,
                text="Mostly stable",
                weight=1,
                explanation="A generally stable income supports home ownership.",
            ),
            ResponseOption(
                id=4,
                text="Very stable",
                weight=3,
                explanation="A predictable income makes it easier to manage a mortgage over many years.",
            ),
        ],
    ),
    Question(
        id=3,
        text="How much have you saved for a home deposit?",
        category="Savings",
        responses=[
            ResponseOption(
                id=1,
                text="Little or no savings",
                weight=-3,
                explanation="A small deposit often leads to higher borrowing costs or difficulty qualifying for a mortgage.",
            ),
            ResponseOption(
                id=2,
                text="Less than 10% of a home's value",
                weight=-1,
                explanation="A smaller deposit may still allow you to buy, but financing is likely to be more expensive.",
            ),
            ResponseOption(
                id=3,
                text="Around 10% to 20%",
                weight=1,
                explanation="A reasonable deposit improves affordability and borrowing terms.",
            ),
            ResponseOption(
                id=4,
                text="More than 20%",
                weight=3,
                explanation="A substantial deposit reduces borrowing costs and financial risk.",
            ),
        ],
    ),
    Question(
        id=4,
        text="How likely are you to relocate for work or personal reasons within the next five years?",
        category="Mobility",
        responses=[
            ResponseOption(
                id=1,
                text="Very likely",
                weight=-3,
                explanation="Frequent relocation generally favours renting because it offers greater flexibility.",
            ),
            ResponseOption(
                id=2,
                text="Somewhat likely",
                weight=-1,
                explanation="Some chance of moving makes renting slightly more attractive.",
            ),
            ResponseOption(
                id=3,
                text="Unlikely",
                weight=1,
                explanation="Staying in one location makes buying more practical.",
            ),
            ResponseOption(
                id=4,
                text="Very unlikely",
                weight=3,
                explanation="Long-term stability strongly favours home ownership.",
            ),
        ],
    ),
    Question(
        id=5,
        text="How comfortable are you paying for maintenance and unexpected repairs?",
        category="Maintenance",
        responses=[
            ResponseOption(
                id=1,
                text="Not comfortable at all",
                weight=-3,
                explanation="Renting usually transfers maintenance responsibilities to the landlord.",
            ),
            ResponseOption(
                id=2,
                text="Somewhat uncomfortable",
                weight=-1,
                explanation="Unexpected repair costs may make renting a better fit.",
            ),
            ResponseOption(
                id=3,
                text="Mostly comfortable",
                weight=1,
                explanation="Being willing to handle maintenance supports buying.",
            ),
            ResponseOption(
                id=4,
                text="Completely comfortable",
                weight=3,
                explanation="Owning a home requires planning for ongoing maintenance expenses.",
            ),
        ],
    ),
    Question(
        id=6,
        text="How important is being able to renovate or customise your home?",
        category="Lifestyle",
        responses=[
            ResponseOption(
                id=1,
                text="Not important",
                weight=-2,
                explanation="If customisation is unimportant, renting may satisfy your housing needs.",
            ),
            ResponseOption(
                id=2,
                text="Slightly important",
                weight=0,
                explanation="Customisation is not a major factor in your decision.",
            ),
            ResponseOption(
                id=3,
                text="Important",
                weight=2,
                explanation="Buying provides much greater freedom to personalise your home.",
            ),
            ResponseOption(
                id=4,
                text="Extremely important",
                weight=3,
                explanation="If creating a long-term personalised home is a priority, buying is generally the better option.",
            ),
        ],
    ),
    Question(
        id=7,
        text="How confident are you that you could comfortably afford monthly mortgage repayments?",
        category="Affordability",
        responses=[
            ResponseOption(
                id=1,
                text="Not confident",
                weight=-3,
                explanation="If mortgage repayments would strain your finances, renting is generally the safer option.",
            ),
            ResponseOption(
                id=2,
                text="Somewhat confident",
                weight=-1,
                explanation="Affordability concerns suggest caution when considering buying.",
            ),
            ResponseOption(
                id=3,
                text="Confident",
                weight=1,
                explanation="Comfortably meeting repayments is an important step toward home ownership.",
            ),
            ResponseOption(
                id=4,
                text="Very confident",
                weight=3,
                explanation="Strong affordability reduces one of the major risks of buying.",
            ),
        ],
    ),
    Question(
        id=8,
        text="How important is the flexibility to move whenever your circumstances change?",
        category="Flexibility",
        responses=[
            ResponseOption(
                id=1,
                text="Extremely important",
                weight=-3,
                explanation="Renting provides the greatest flexibility when life circumstances change.",
            ),
            ResponseOption(
                id=2,
                text="Somewhat important",
                weight=-1,
                explanation="A preference for flexibility slightly favours renting.",
            ),
            ResponseOption(
                id=3,
                text="Not very important",
                weight=1,
                explanation="If flexibility is less important, buying becomes more attractive.",
            ),
            ResponseOption(
                id=4,
                text="Not important at all",
                weight=3,
                explanation="If you prefer long-term stability, home ownership may suit you well.",
            ),
        ],
    ),
    Question(
        id=9,
        text="How comfortable are you taking on financial risk in pursuit of long-term financial gain?",
        category="Risk Tolerance",
        responses=[
            ResponseOption(
                id=1,
                text="Not comfortable at all",
                weight=-3,
                explanation="Buying a home involves financial risks such as property value changes, interest rate fluctuations, and unexpected maintenance costs. If you prefer to minimise financial risk, renting may be more suitable.",
            ),
            ResponseOption(
                id=2,
                text="Slightly comfortable",
                weight=-1,
                explanation="A cautious attitude toward financial risk makes renting a slightly better fit, as it generally involves fewer long-term financial uncertainties.",
            ),
            ResponseOption(
                id=3,
                text="Moderately comfortable",
                weight=1,
                explanation="Being willing to accept some financial risk can make buying a reasonable option if your overall finances are strong.",
            ),
            ResponseOption(
                id=4,
                text="Very comfortable",
                weight=3,
                explanation="If you're comfortable accepting financial risk in exchange for potential long-term benefits such as building equity and property appreciation, buying may be well suited to your goals.",
            ),
        ],
    ),
    Question(
        id=10,
        text="How settled do you expect your lifestyle to be over the next 5 to 10 years?",
        category="Life Stability",
        responses=[
            ResponseOption(
                id=1,
                text="Very uncertain",
                weight=-3,
                explanation="If your lifestyle is likely to change significantly, renting offers greater flexibility.",
            ),
            ResponseOption(
                id=2,
                text="Somewhat uncertain",
                weight=-1,
                explanation="Some uncertainty makes renting slightly more attractive.",
            ),
            ResponseOption(
                id=3,
                text="Mostly settled",
                weight=1,
                explanation="A stable lifestyle makes buying more practical.",
            ),
            ResponseOption(
                id=4,
                text="Very settled",
                weight=3,
                explanation="A stable long-term lifestyle strongly supports buying a home.",
            ),
        ],
    ),
]
