from openai import OpenAI

# Initialise le client DeepSeek
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

def query_deepseek(prompt: str) -> str:
    """Appelle l'API DeepSeek et retourne la réponse complète."""
    completion = client.chat.completions.create(
        model="deepseek-ai/deepseek-v3.1-terminus",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        top_p=0.7,
        max_tokens=8192,
        extra_body={"chat_template_kwargs": {"thinking": True}},
        stream=True
    )

    response_text = ""
    for chunk in completion:
        reasoning = getattr(chunk.choices[0].delta, "reasoning_content", None)
        if reasoning:
            response_text += reasoning
        if chunk.choices[0].delta.content is not None:
            response_text += chunk.choices[0].delta.content
    return response_text
