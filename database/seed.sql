-- Sample Challenge Data for PromptMaster
-- Run this after running schema.sql

-- Creative Writing Challenges
INSERT INTO challenges (category, title, description, goal, example_prompt, difficulty) VALUES
(
    'Creative Writing',
    'Short Story Opening',
    'Write a compelling opening paragraph for a sci-fi short story',
    'Generate an engaging first paragraph that hooks the reader and establishes the setting',
    'Write the opening paragraph of a science fiction story set in the year 2150. The story should begin on a space station orbiting Mars. Include sensory details and introduce a sense of mystery. The tone should be suspenseful but not dark. Aim for 100-150 words.',
    'beginner'
),
(
    'Creative Writing',
    'Character Description',
    'Create a detailed character description for a fantasy novel',
    'Generate a vivid, multi-dimensional character description including physical traits, personality, and background',
    'Create a detailed character description for a fantasy novel protagonist. Include: physical appearance (age, build, distinctive features), personality traits (3-4 key characteristics), background (occupation, family), and a unique quirk or habit. The character should be a female warrior in her late 20s. Write in third person, 200-250 words.',
    'intermediate'
),
(
    'Creative Writing',
    'Dialogue Scene',
    'Write a tense dialogue between two characters with conflicting goals',
    'Generate realistic, character-driven dialogue that reveals personality and advances conflict',
    'Write a dialogue scene between two characters: a detective interrogating a suspect in a theft case. The suspect is nervous but trying to appear confident. Include: stage directions in brackets, subtext (what they really mean vs. what they say), and a twist at the end. 300-400 words. Focus on tension and pacing.',
    'advanced'
);

-- Coding & Debugging Challenges
INSERT INTO challenges (category, title, description, goal, example_prompt, difficulty) VALUES
(
    'Coding & Debugging',
    'Function Documentation',
    'Generate clear documentation for a Python function',
    'Create comprehensive docstring that explains purpose, parameters, returns, and examples',
    'Write a detailed docstring for a Python function named "calculate_discount" that takes three parameters: price (float), discount_percentage (float), and min_purchase (float). The function should return the discounted price only if the price meets the minimum purchase requirement. Include: function description, parameters with types, return value with type, example usage, and edge cases. Follow Google style docstring format.',
    'beginner'
),
(
    'Coding & Debugging',
    'Bug Fix Explanation',
    'Analyze code with a bug and explain the issue',
    'Identify the bug, explain why it occurs, and provide a corrected version with explanation',
    'Analyze this Python code that is supposed to calculate average but returns incorrect results:\n\ndef calculate_average(numbers):\n    total = 0\n    for num in numbers:\n        total += num\n    return total / len(numbers)\n\naverage = calculate_average([])\n\nExplain: 1) What bug exists, 2) Why it causes an error, 3) Provide corrected code with comments, 4) Suggest how to prevent similar issues. Be specific and educational.',
    'intermediate'
),
(
    'Coding & Debugging',
    'Algorithm Optimization',
    'Optimize a given algorithm for better performance',
    'Analyze time complexity, identify bottlenecks, and provide optimized solution',
    'Optimize this Python function that finds duplicates in a list:\n\ndef find_duplicates(lst):\n    duplicates = []\n    for i in range(len(lst)):\n        for j in range(i + 1, len(lst)):\n            if lst[i] == lst[j] and lst[i] not in duplicates:\n                duplicates.append(lst[i])\n    return duplicates\n\nProvide: 1) Current time complexity analysis, 2) Bottlenecks identified, 3) Optimized solution using appropriate data structures, 4) New time complexity, 5) Trade-offs if any. Include code comments explaining the optimization.',
    'advanced'
);

-- Summarization & Rewriting Challenges
INSERT INTO challenges (category, title, description, goal, example_prompt, difficulty) VALUES
(
    'Summarization & Rewriting',
    'Article Summary',
    'Summarize a news article into key points',
    'Create a concise summary that captures main ideas and important details',
    'Summarize this article about renewable energy in 3-5 bullet points:\n\n[Article text here]\n\nRequirements: Each bullet should be one sentence, capture essential information only, maintain objective tone, prioritize facts over opinions, and be suitable for a general audience. Total length: 75-100 words.',
    'beginner'
),
(
    'Summarization & Rewriting',
    'Tone Conversion',
    'Rewrite a formal email in casual tone',
    'Transform professional language while maintaining core message and clarity',
    'Rewrite this formal business email in a casual, friendly tone suitable for a colleague:\n\n[Email text here]\n\nRequirements: Keep the same structure (greeting, body, closing), maintain all important information, make it sound conversational but still professional, use contractions where appropriate, aim for warmth without being overly familiar. Length should be similar to original.',
    'intermediate'
),
(
    'Summarization & Rewriting',
    'Technical to Layman',
    'Translate technical jargon into simple language',
    'Explain complex technical concepts in accessible terms without losing accuracy',
    'Translate this technical description of blockchain into simple language for a non-technical audience:\n\n[Technical text here]\n\nRequirements: Remove all jargon or explain it in parentheses, use analogies to everyday experiences, maintain technical accuracy, assume reader has no background knowledge, make it engaging and easy to understand. Target: 8th grade reading level. 150-200 words.',
    'advanced'
);

-- Data Extraction Challenges
INSERT INTO challenges (category, title, description, goal, example_prompt, difficulty) VALUES
(
    'Data Extraction',
    'Contact Information',
    'Extract contact details from unstructured text',
    'Identify and format names, emails, and phone numbers consistently',
    'Extract all contact information from this text and format as JSON:\n\n"Please contact John Smith at john.smith@email.com or call (555) 123-4567. For urgent matters, reach out to Sarah Johnson: sarah.j@company.com, phone: 555-987-6543."\n\nOutput format:\n{\n  "contacts": [\n    {\n      "name": "",\n      "email": "",\n      "phone": ""\n    }\n  ]\n}\n\nEnsure: All fields present for each contact, phone numbers in (XXX) XXX-XXXX format, valid JSON syntax.',
    'beginner'
),
(
    'Data Extraction',
    'Product Details',
    'Parse product information into structured format',
    'Extract product attributes and organize hierarchically',
    'Extract product information from this description into structured JSON:\n\n[Product description here]\n\nRequired fields: product_name, category, price, specifications (as nested object), features (as array), availability. Format prices with currency symbol, standardize units of measurement, handle missing data with null values. Ensure valid JSON with proper nesting and arrays where appropriate.',
    'intermediate'
),
(
    'Data Extraction',
    'Complex Data Parsing',
    'Extract and normalize data from mixed format documents',
    'Handle multiple data types, resolve inconsistencies, and create clean output',
    'Extract and normalize data from this multi-format document containing both tabular and narrative sections:\n\n[Complex document here]\n\nTasks: 1) Identify all entities (people, organizations, dates, amounts), 2) Resolve any inconsistent formatting, 3) Create a normalized JSON structure with: entities array, relationships between entities, timeline of events, financial data summary. Handle edge cases like missing data, ambiguous references, and format variations. Output should be valid JSON with clear schema.',
    'advanced'
);

-- Add some metadata comments
COMMENT ON TABLE challenges IS 'Stores prompt engineering challenges across different categories and difficulty levels';
COMMENT ON COLUMN challenges.category IS 'Challenge category: Creative Writing, Coding & Debugging, Summarization & Rewriting, or Data Extraction';
COMMENT ON COLUMN challenges.difficulty IS 'Difficulty level: beginner, intermediate, or advanced';
COMMENT ON COLUMN challenges.example_prompt IS 'Example of a well-crafted prompt for this challenge';
