from guardrails import Guard, OnFailAction
from guardrails.hub import CompetitorCheck, ToxicLanguage

guard = Guard().use_many(
    CompetitorCheck(["Apple", "Microsoft", "Google"], on_fail=OnFailAction.EXCEPTION),
    ToxicLanguage(threshold=0.5, validation_method="sentence", on_fail=OnFailAction.EXCEPTION)
)

guard.validate(
    """An apple a day keeps a doctor away.
    This is good advice for keeping your health."""
)  # Both the guardrails pass

try:
    guard.validate(
        """Shut the hell up! Apple just released a new iPhone."""
    )  # Both the guardrails fail
except Exception as e:
    print(e)

# from guardrails import Guard, OnFailAction
# from guardrails.hub import RegexMatch

# guard = Guard().use(
#     RegexMatch, regex="\(?\d{3}\)?-? *\d{3}-? *-?\d{4}", on_fail=OnFailAction.EXCEPTION
# )

# guard.validate("123-456-7890")  # Guardrail passes

# try:
#     guard.validate("1234-789-0000")  # Guardrail fails
# except Exception as e:
#     print(e)