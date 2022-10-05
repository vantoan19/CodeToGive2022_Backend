import os
from time import sleep

import requests

HOST_DOMAIN = os.environ.get("HOST_DOMAIN")

labels = [
    {
        "label": "Intellectuality",
        "type": "NON_REQUIRED_LABEL",
        "category": "MOTIVATION_LABEL",
        "description": "Intellectuality label",
    },
    {
        "label": "Altruism/Caring",
        "type": "NON_REQUIRED_LABEL",
        "category": "MOTIVATION_LABEL",
        "description": "Altruism/Caring label",
    },
    {
        "label": "Finances/Money",
        "type": "NON_REQUIRED_LABEL",
        "category": "MOTIVATION_LABEL",
        "description": "Finances/Money label",
    },
    {
        "label": "Variety",
        "type": "NON_REQUIRED_LABEL",
        "category": "MOTIVATION_LABEL",
        "description": "Variety label",
    },
    {
        "label": "Independence",
        "type": "NON_REQUIRED_LABEL",
        "category": "MOTIVATION_LABEL",
        "description": "Independence label",
    },
    {
        "label": "Prestige",
        "type": "NON_REQUIRED_LABEL",
        "category": "MOTIVATION_LABEL",
        "description": "Prestige label",
    },
    {
        "label": "Aesthetics",
        "type": "NON_REQUIRED_LABEL",
        "category": "MOTIVATION_LABEL",
        "description": "Aesthetics label",
    },
    {
        "label": "Relationships",
        "type": "NON_REQUIRED_LABEL",
        "category": "MOTIVATION_LABEL",
        "description": "Relationships label",
    },
    {
        "label": "Playfulness",
        "type": "NON_REQUIRED_LABEL",
        "category": "MOTIVATION_LABEL",
        "description": "Playfulness label",
    },
    {
        "label": "Self-fulfilment",
        "type": "NON_REQUIRED_LABEL",
        "category": "MOTIVATION_LABEL",
        "description": "Self-fulfilment label",
    },
    {
        "label": "Hierarchy",
        "type": "NON_REQUIRED_LABEL",
        "category": "MOTIVATION_LABEL",
        "description": "Hierarchy label",
    },
    {
        "label": "Human values",
        "type": "NON_REQUIRED_LABEL",
        "category": "MOTIVATION_LABEL",
        "description": "Human values label",
    },
    {
        "label": "Job performance",
        "type": "NON_REQUIRED_LABEL",
        "category": "MOTIVATION_LABEL",
        "description": "Job performance label",
    },
    {
        "label": "Creativity",
        "type": "NON_REQUIRED_LABEL",
        "category": "MOTIVATION_LABEL",
        "description": "Creativity label",
    },
    {
        "label": "Leadership",
        "type": "NON_REQUIRED_LABEL",
        "category": "MOTIVATION_LABEL",
        "description": "Leadership label",
    },
]

motivation_questions = [
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Intellectuality"],
        "description": "I would like to have a job, where I continuously face new and unsolved problems.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Intellectuality"],
        "description": "I would like to have a job, where I meet new ideas.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Intellectuality"],
        "description": "I would like to have a job, where I can do an intellectually challenging job.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Altruism/Caring"],
        "description": "I would like to have a job, where I can help others.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Altruism/Caring"],
        "description": "I would like to have a job, where I can do good for the common interest.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Altruism/Caring"],
        "description": "I would like to have a job, where people benefit from my work.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Finances/Money"],
        "description": "I would like to have a job, where I can make a lot of money.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Finances/Money"],
        "description": "I would like to have a job, where I can provide myself with a carefree life.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Finances/Money"],
        "description": "I would like to have a job, where I can expect a valuable pension.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Variety"],
        "description": "I would like to have a job, where I can do varied tasks.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Variety"],
        "description": "I would like to have a job, where I don't have to do repetitive tasks.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Variety"],
        "description": "I would like to have a job, where I can keep myself busy with a variety of tasks.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Independence"],
        "description": "I would like to have a job, where I can make decisions independently in the scope of my work.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Independence"],
        "description": "I would like to have a job, where I can make independent decisions.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Independence"],
        "description": "I would like to have a job, where other people cannot control how I work.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Prestige"],
        "description": "I would like to have a job, where I can earn credit for my work.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Prestige"],
        "description": "I would like to have a job, where I can make sure that my work will be honoured.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Prestige"],
        "description": "I would like to have a job, where people look up to me.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Aesthetics"],
        "description": "I would like to have a job, where I could become an artist.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Aesthetics"],
        "description": "I would like to have a job, where I can make the world a better place.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Aesthetics"],
        "description": "I would like to have a job, where I can make something beautiful.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Relationships"],
        "description": "I would like to have a job, where I am a part of a community.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Relationships"],
        "description": "I would like to have a job, where my coworkers are my friends, too.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Relationships"],
        "description": "I would like to have a job, where I have a good relationship with my coworkers.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Playfulness"],
        "description": "I would like to have a job, where I can make decisions based on my emotions.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Playfulness"],
        "description": "I would like to have a job, where I can do tasks which might seem insignificant to others.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Playfulness"],
        "description": "I would like to have a job, where I can play sometimes.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Self-fulfilment"],
        "description": "I would like to have a job, where I can fulfil myself.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Self-fulfilment"],
        "description": "I would like to have a job, where I can utilise my personal lifestyle.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Self-fulfilment"],
        "description": "I would like to have a job, where I can live my best life.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Hierarchy"],
        "description": "I would like to have a job, where I can respect my boss.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Hierarchy"],
        "description": "I would like to have a job, where my boss will always make the right calls.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Hierarchy"],
        "description": "I would like to have a job, where my boss is sympathetic.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Human values"],
        "description": "I would like to have a job, where I can contribute to social justice.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Human values"],
        "description": "I would like to have a job, where my successes and failures will be evaluated by future generations.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Human values"],
        "description": "I would like to have a job, where I need to manage conflicts.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Job performance"],
        "description": "I would like to have a job, where I can figure out good or bad solutions. ?",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Job performance"],
        "description": "I would like to have a job, where I can objectively measure the quality of my work.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Job performance"],
        "description": "I would like to have a job, where I can continuously learn.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Creativity"],
        "description": "I would like to have a job, where I can bring new ideas.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Creativity"],
        "description": "I would like to have a job, where I can invent something new.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Creativity"],
        "description": "I would like to have a job, where I can always contribute with new ideas.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Leadership"],
        "description": "I would like to have a job, where I can lead others.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Leadership"],
        "description": "I would like to have a job, where I might need leadership skills.",
    },
    {
        "type": "MOTIVATION_QUESTION",
        "labels": ["Leadership"],
        "description": "I would like to have a job, where I can supervise other people's work.",
    },
]

jobs = [
    {
        "title": "Librarian",
        "description": "U will need to do this, and that, this skill, that skill",
        "company_name": "Canary inc",
        "company_about": "This company is legit, no cap, 4real",
        "image": "https://images.unsplash.com/photo-1507842217343-583bb7270b66?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8bGlicmFyeXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "labels": [
            {
                "label": "Intellectuality",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Altruism/Caring",
                "lower_importance_bound": 4,
                "upper_importance_bound": 5,
            },
            {
                "label": "Finances/Money",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Variety",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Independence",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Prestige",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Aesthetics",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Relationships",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Playfulness",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Self-fulfilment",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Hierarchy",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Human values",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Job performance",
                "lower_importance_bound": 2,
                "upper_importance_bound": 5,
            },
            {
                "label": "Creativity",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Leadership",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
        ],
        "address": {
            "street_line_1": "Kiraly utca",
            "district": "VI",
            "city": "Budapest",
            "region": "Budapest",
            "country": "Hungary",
        },
    },
    {
        "title": "Receptionist",
        "description": "Answer the phone, make some copies,etc",
        "company_name": "Dunder Mifflin Inc",
        "company_about": "Paper company",
        "image": "https://images.unsplash.com/photo-1556741533-6e6a62bd8b49?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cmVjZXB0aW9uaXN0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
        "labels": [
            {
                "label": "Intellectuality",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Altruism/Caring",
                "lower_importance_bound": 4,
                "upper_importance_bound": 5,
            },
            {
                "label": "Finances/Money",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Variety",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Independence",
                "lower_importance_bound": 2,
                "upper_importance_bound": 5,
            },
            {
                "label": "Prestige",
                "lower_importance_bound": 4,
                "upper_importance_bound": 5,
            },
            {
                "label": "Aesthetics",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Relationships",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Playfulness",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Self-fulfilment",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Hierarchy",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Human values",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Job performance",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Creativity",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Leadership",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
        ],
        "address": {
            "street_line_1": "Dob utca",
            "district": "VI",
            "city": "Budapest",
            "region": "Budapest",
            "country": "Hungary",
        },
    },
    {
        "title": "Bartender",
        "description": "Make and serves drinks",
        "company_name": "Black Box",
        "company_about": "Club",
        "image": "https://images.unsplash.com/photo-1595751866979-de6e9d606220?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8YmFydGVuZGVyfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
        "labels": [
            {
                "label": "Intellectuality",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Altruism/Caring",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Finances/Money",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Variety",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Independence",
                "lower_importance_bound": 2,
                "upper_importance_bound": 5,
            },
            {
                "label": "Prestige",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Aesthetics",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Relationships",
                "lower_importance_bound": 4,
                "upper_importance_bound": 5,
            },
            {
                "label": "Playfulness",
                "lower_importance_bound": 4,
                "upper_importance_bound": 5,
            },
            {
                "label": "Self-fulfilment",
                "lower_importance_bound": 2,
                "upper_importance_bound": 5,
            },
            {
                "label": "Hierarchy",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Human values",
                "lower_importance_bound": 2,
                "upper_importance_bound": 5,
            },
            {
                "label": "Job performance",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Creativity",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Leadership",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
        ],
        "address": {
            "street_line_1": "Joszef korut",
            "district": "V",
            "city": "Budapest",
            "region": "Budapest",
            "country": "Hungary",
        },
    },
    {
        "title": "Liquid Chemical Tanker Truck Driver",
        "description": "Must have a clean driving record class A CDL twic card hazmat plus at least 3-5 years experience in hotshot",
        "company_name": "Tankstar USA, Inc",
        "company_about": "Tankstar USA, Inc. and affiliated companies, (including Schwerman Trucking Co., Rogers Cartage Co., North American Bulk Transport, Inc. and Bulk Logistics, Inc.), as Responsible Care Partners, are dedicated to the safe transport of bulk commodities. As one of the oldest and largest tank truck carriers in the nation, we have a long history of providing quality service. For us, an integral part of quality service is operating in a manner that protects the environment and safeguards the health, safety, and security of employees, customers, and the communities where we operate.",
        "image": "https://images.unsplash.com/photo-1595751866979-de6e9d606220?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8YmFydGVuZGVyfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
        "labels": [
            {
                "label": "Intellectuality",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Altruism/Caring",
                "lower_importance_bound": 2,
                "upper_importance_bound": 5,
            },
            {
                "label": "Finances/Money",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Variety",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Independence",
                "lower_importance_bound": 2,
                "upper_importance_bound": 5,
            },
            {
                "label": "Prestige",
                "lower_importance_bound": 2,
                "upper_importance_bound": 5,
            },
            {
                "label": "Aesthetics",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Relationships",
                "lower_importance_bound": 2,
                "upper_importance_bound": 5,
            },
            {
                "label": "Playfulness",
                "lower_importance_bound": 2,
                "upper_importance_bound": 5,
            },
            {
                "label": "Self-fulfilment",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Hierarchy",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Human values",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Job performance",
                "lower_importance_bound": 4,
                "upper_importance_bound": 5,
            },
            {
                "label": "Creativity",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Leadership",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
        ],
        "address": {
            "street_line_1": "Vietnam utca",
            "district": "V",
            "city": "Budapest",
            "region": "Budapest",
            "country": "Hungary",
        },
    },
    {
        "title": "Tailor",
        "description": "Make dresses for women and childs",
        "company_name": "Clinic Textiles and tailors",
        "company_about": "We're all about making good, quality custom clothing to be worn and loved over time. We're passionate about changing the way you look at clothing and changing the way they're made. We want nothing more than for you to join us. It's time to start wearing clothes that fit, for real.",
        "image": "https://plus.unsplash.com/premium_photo-1663050981532-613cd5e4cc91?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8dGFpbG9yfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
        "labels": [
            {
                "label": "Intellectuality",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Altruism/Caring",
                "lower_importance_bound": 4,
                "upper_importance_bound": 5,
            },
            {
                "label": "Finances/Money",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Variety",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Independence",
                "lower_importance_bound": 2,
                "upper_importance_bound": 5,
            },
            {
                "label": "Prestige",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Aesthetics",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Relationships",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Playfulness",
                "lower_importance_bound": 2,
                "upper_importance_bound": 5,
            },
            {
                "label": "Self-fulfilment",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Hierarchy",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Human values",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Job performance",
                "lower_importance_bound": 4,
                "upper_importance_bound": 5,
            },
            {
                "label": "Creativity",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Leadership",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
        ],
        "address": {
            "street_line_1": "Vietnam utca",
            "district": "V",
            "city": "Budapest",
            "region": "Budapest",
            "country": "Hungary",
        },
    },
    {
        "title": "Public Works Utility Worker",
        "description": "Performs manual and semi-skilled work involving maintenance, construction, installation, and repair related to water, sewer and storm system lines, water courses, facilities and equipment; and water, sewer and storm watershed areas; transports materials to and from worksites and City-owned facilities; and performs general maintenance work and related work as required.",
        "company_name": "CITY OF NEW BRITAIN",
        "company_about": "CITY OF NEW BRITAIN CIVIL SERVICE COMMISSION",
        "image": "https://images.unsplash.com/photo-1519226271816-35674b1074db?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8d29vZCUyMGN1dHRlcnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "labels": [
            {
                "label": "Intellectuality",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Altruism/Caring",
                "lower_importance_bound": 4,
                "upper_importance_bound": 5,
            },
            {
                "label": "Finances/Money",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Variety",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Independence",
                "lower_importance_bound": 2,
                "upper_importance_bound": 5,
            },
            {
                "label": "Prestige",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Aesthetics",
                "lower_importance_bound": 2,
                "upper_importance_bound": 5,
            },
            {
                "label": "Relationships",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Playfulness",
                "lower_importance_bound": 2,
                "upper_importance_bound": 5,
            },
            {
                "label": "Self-fulfilment",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Hierarchy",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Human values",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Job performance",
                "lower_importance_bound": 4,
                "upper_importance_bound": 5,
            },
            {
                "label": "Creativity",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Leadership",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
        ],
        "address": {
            "street_line_1": "Hungarian utca",
            "district": "V",
            "city": "Budapest",
            "region": "Budapest",
            "country": "Hungary",
        },
    },
    {
        "title": "Hair Salon Manager",
        "description": "Allertons has just celebrated our 8th Anniversary, and we are looking for a Full Time Hair Salon Manager to join our fourth and newest salon in Harrogate City Centre. Come and join our positive, professional and productive team with support, encouragement, training, bonuses and more.",
        "company_name": "Allertons",
        "company_about": "Allertons is unique - Everything Beauty For Her, Him and Home. Allertons provides unisex services in Hair, Facials, Massage, Waxing, Brows, Lashes and Nails, as well as stocking the worlds leading Skincare, Makeup, Haircare, Fragrance and Home products. Because of this, we look for a team of people who are just as unique, with a true passion for Beauty.",
        "image": "https://images.unsplash.com/photo-1580618672591-eb180b1a973f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8aGFpciUyMHN0eWxpc3R8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60",
        "labels": [
            {
                "label": "Intellectuality",
                "lower_importance_bound": 2,
                "upper_importance_bound": 5,
            },
            {
                "label": "Altruism/Caring",
                "lower_importance_bound": 4,
                "upper_importance_bound": 5,
            },
            {
                "label": "Finances/Money",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Variety",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Independence",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Prestige",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Aesthetics",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Relationships",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Playfulness",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Self-fulfilment",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Hierarchy",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Human values",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Job performance",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Creativity",
                "lower_importance_bound": 4,
                "upper_importance_bound": 5,
            },
            {
                "label": "Leadership",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
        ],
        "address": {
            "street_line_1": "This utca",
            "district": "V",
            "city": "Budapest",
            "region": "Budapest",
            "country": "Hungary",
        },
    },
    {
        "title": "Financial Reporting Manager",
        "description": "The Financial Reporting Manager will be responsible for the management of the preparation of daily, weekly, monthly and quarterly returns to Central Banks and other policymakers in multiple countries in the EMEA region.",
        "company_name": "Citi Group",
        "company_about": "Citi, the leading global bank, serves more than 200 million customer accounts and does business in more than 160 countries and jurisdictions.",
        "image": "https://images.unsplash.com/photo-1526628953301-3e589a6a8b74?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZmluYW5jaWFsJTIwcmVwb3J0aW5nJTIwbWFuYWdlcnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "labels": [
            {
                "label": "Intellectuality",
                "lower_importance_bound": 4,
                "upper_importance_bound": 5,
            },
            {
                "label": "Altruism/Caring",
                "lower_importance_bound": 5,
                "upper_importance_bound": 5,
            },
            {
                "label": "Finances/Money",
                "lower_importance_bound": 4,
                "upper_importance_bound": 5,
            },
            {
                "label": "Variety",
                "lower_importance_bound": 2,
                "upper_importance_bound": 5,
            },
            {
                "label": "Independence",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Prestige",
                "lower_importance_bound": 4,
                "upper_importance_bound": 5,
            },
            {
                "label": "Aesthetics",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Relationships",
                "lower_importance_bound": 4,
                "upper_importance_bound": 5,
            },
            {
                "label": "Playfulness",
                "lower_importance_bound": 2,
                "upper_importance_bound": 5,
            },
            {
                "label": "Self-fulfilment",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Hierarchy",
                "lower_importance_bound": 2,
                "upper_importance_bound": 5,
            },
            {
                "label": "Human values",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Job performance",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Creativity",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Leadership",
                "lower_importance_bound": 4,
                "upper_importance_bound": 5,
            },
        ],
        "address": {
            "street_line_1": "That utca",
            "district": "V",
            "city": "Budapest",
            "region": "Budapest",
            "country": "Hungary",
        },
    },
    {
        "title": "Senior Finance Specialist",
        "description": "We are looking for a talented Finance, Risk, or Reporting professional to join the Finance Special Tactics Team and go on business continuity assignments across various Finance teams. The Special Tactics team is an internal consulting unit serving Citi entities in the EMEA region where we use Python, KNIME and other digital tools to solve our problems.",
        "company_name": "Citi Group",
        "company_about": "Citi, the leading global bank, serves more than 200 million customer accounts and does business in more than 160 countries and jurisdictions.",
        "image": "https://images.unsplash.com/photo-1444653614773-995cb1ef9efa?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8c2VuaW9yJTIwZmluYW5jZSUyMHNwZWNpYWxpc3R8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60",
        "labels": [
            {
                "label": "Intellectuality",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Altruism/Caring",
                "lower_importance_bound": 4,
                "upper_importance_bound": 5,
            },
            {
                "label": "Finances/Money",
                "lower_importance_bound": 4,
                "upper_importance_bound": 5,
            },
            {
                "label": "Variety",
                "lower_importance_bound": 2,
                "upper_importance_bound": 5,
            },
            {
                "label": "Independence",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Prestige",
                "lower_importance_bound": 4,
                "upper_importance_bound": 5,
            },
            {
                "label": "Aesthetics",
                "lower_importance_bound": 1,
                "upper_importance_bound": 5,
            },
            {
                "label": "Relationships",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Playfulness",
                "lower_importance_bound": 2,
                "upper_importance_bound": 5,
            },
            {
                "label": "Self-fulfilment",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Hierarchy",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Human values",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Job performance",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Creativity",
                "lower_importance_bound": 3,
                "upper_importance_bound": 5,
            },
            {
                "label": "Leadership",
                "lower_importance_bound": 2,
                "upper_importance_bound": 5,
            },
        ],
        "address": {
            "street_line_1": "That utca",
            "district": "V",
            "city": "Budapest",
            "region": "Budapest",
            "country": "Hungary",
        },
    },
]


for label in labels:
    requests.post(url=f"http://34.116.151.108/api/v1/labels/", json=label)
    sleep(1)

for question in motivation_questions:
    requests.post(
        url=f"http://34.116.151.108/api/v1/questions/motivation-question", json=question
    )
    sleep(1)

for job in jobs:
    requests.post(url=f"http://34.116.151.108/api/v1/jobs/", json=job)
    sleep(1)
