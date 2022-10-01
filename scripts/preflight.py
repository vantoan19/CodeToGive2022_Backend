import os
from time import sleep

import requests

HOST_DOMAIN = os.environ.get("HOST_DOMAIN")

labels = [
    {
        "label": "Intellectuality",
        "type": "NON_REQUIRED_LABEL",
        "description": "Intellectuality label"
    },
    {
        "label": "Altruism/Caring",
        "type": "NON_REQUIRED_LABEL",
        "description": "Altruism/Caring label"
    },
    {
        "label": "Finances/Money",
        "type": "NON_REQUIRED_LABEL",
        "description": "Finances/Money label"
    },
    {
        "label": "Variety",
        "type": "NON_REQUIRED_LABEL",
        "description": "Variety label"
    },
    {
        "label": "Independence",
        "type": "NON_REQUIRED_LABEL",
        "description": "Independence label"
    },
    {
        "label": "Prestige",
        "type": "NON_REQUIRED_LABEL",
        "description": "Prestige label"
    },
    {
        "label": "Aesthetics",
        "type": "NON_REQUIRED_LABEL",
        "description": "Aesthetics label"
    },
    {
        "label": "Relationships",
        "type": "NON_REQUIRED_LABEL",
        "description": "Relationships label"
    },
    {
        "label": "Playfulness",
        "type": "NON_REQUIRED_LABEL",
        "description": "Playfulness label"
    },
    {
        "label": "Self-fulfilment",
        "type": "NON_REQUIRED_LABEL",
        "description": "Self-fulfilment label"
    },
    {
        "label": "Hierarchy",
        "type": "NON_REQUIRED_LABEL",
        "description": "Hierarchy label"
    },
    {
        "label": "Human values",
        "type": "NON_REQUIRED_LABEL",
        "description": "Human values label"
    },
    {
        "label": "Job performance",
        "type": "NON_REQUIRED_LABEL",
        "description": "Job performance label"
    },
    {
        "label": "Creativity",
        "type": "NON_REQUIRED_LABEL",
        "description": "Creativity label"
    },
    {
        "label": "Leadership",
        "type": "NON_REQUIRED_LABEL",
        "description": "Leadership label"
    }
]

motivation_questions = [
    {
        "description": "I would like to have a job, where I continuously face new and unsolved problems.",
        "labels": ["Intellectuality"]
    },
    {
        "description": "I would like to have a job, where I can others.",
        "labels": ["Altruism/Caring"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can make a lot of money.",
        "labels": ["Finances/Money"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I do varied tasks.",
        "labels": ["Variety"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can make decisions independently in the scope of my work.",
        "labels": ["Independence"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can earn credit for my work.",
        "labels": ["Prestige"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I could become an artist.",
        "labels": ["Aesthetics"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I a part of a community.",
        "labels": ["Relationships"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can make decisions based on my emotions",
        "labels": ["Playfulness"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can fulfil myself.",
        "labels": ["Self-fulfilment"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can respect my boss.",
        "labels": ["Hierarchy"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can contribute to social justice.",
        "labels": ["Human values"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can figure out good or bad solutions.",
        "labels": ["Job performance"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can bring new ideas",
        "labels": ["Creativity"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can lead other.",
        "labels": ["Leadership"]
    },
    {
        "description": "I would like to have a job, where I continuously face new and unsolved problems.",
        "labels": ["Intellectuality"]
    },
    {
        "description": "I would like to have a job, where I can others.",
        "labels": ["Altruism/Caring"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can make a lot of money.",
        "labels": ["Finances/Money"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I do varied tasks.",
        "labels": ["Variety"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can make decisions independently in the scope of my work.",
        "labels": ["Independence"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can earn credit for my work.",
        "labels": ["Prestige"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I could become an artist.",
        "labels": ["Aesthetics"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I a part of a community.",
        "labels": ["Relationships"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can make decisions based on my emotions",
        "labels": ["Playfulness"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can fulfil myself.",
        "labels": ["Self-fulfilment"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can respect my boss.",
        "labels": ["Hierarchy"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can contribute to social justice.",
        "labels": ["Human values"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can figure out good or bad solutions.",
        "labels": ["Job performance"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can bring new ideas",
        "labels": ["Creativity"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can lead other.",
        "labels": ["Leadership"]
    },
    {
        "description": "I would like to have a job, where I continuously face new and unsolved problems.",
        "labels": ["Intellectuality"]
    },
    {
        "description": "I would like to have a job, where I can others.",
        "labels": ["Altruism/Caring"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can make a lot of money.",
        "labels": ["Finances/Money"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I do varied tasks.",
        "labels": ["Variety"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can make decisions independently in the scope of my work.",
        "labels": ["Independence"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can earn credit for my work.",
        "labels": ["Prestige"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I could become an artist.",
        "labels": ["Aesthetics"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I a part of a community.",
        "labels": ["Relationships"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can make decisions based on my emotions",
        "labels": ["Playfulness"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can fulfil myself.",
        "labels": ["Self-fulfilment"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can respect my boss.",
        "labels": ["Hierarchy"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can contribute to social justice.",
        "labels": ["Human values"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can figure out good or bad solutions.",
        "labels": ["Job performance"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can bring new ideas",
        "labels": ["Creativity"]
    },
    {
        "type": "MOTIVATION_QUESTION",
        "description": "I would like to have a job, where I can lead other.",
        "labels": ["Leadership"]
    },
]

for label in labels:
    requests.post(url=f"{HOST_DOMAIN}/api/v1/labels/", json=label)
    sleep(1)
    
for question in motivation_questions:
    requests.post(url=f"{HOST_DOMAIN}/api/v1/questions/motivation-question", json=question)
    sleep(1)
