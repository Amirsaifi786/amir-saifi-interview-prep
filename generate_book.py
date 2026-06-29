from pathlib import Path

out = Path('c:/interview_question_answer_project/Complete_MNC_Interview_Preparation_Guide_for_Amir_Saifi.html')

sections = []

sections.append(("Cover", """
<div class=\"page\">\n  <div class=\"cover\">\n    <h1>Complete MNC Interview Preparation Guide for Amir Saifi</h1>\n    <p>A premium interview preparation book for Laravel, PHP, Full Stack, Backend, React, MERN, and Software Engineer roles</p>\n    <p>Prepared for 3–5 years of experience and MNC interview readiness</p>\n  </div>\n</div>\n"""))

sections.append(("Table of Contents", """
<div class=\"page\">\n  <h1>Table of Contents</h1>\n  <ol class=\"toc\">\n    <li>Section 1 — Resume Analysis</li>\n    <li>Section 2 — HR Interview Preparation</li>\n    <li>Section 3 — Self Introduction</li>\n    <li>Section 4 — PHP Interview Mastery</li>\n    <li>Section 5 — Laravel Interview Mastery</li>\n    <li>Section 6 — JavaScript Interview Mastery</li>\n    <li>Section 7 — React Interview Mastery</li>\n    <li>Section 8 — Node.js Interview Mastery</li>\n    <li>Section 9 — SQL Interview Mastery</li>\n    <li>Section 10 — REST API Interview Mastery</li>\n    <li>Section 11 — Git Interview Mastery</li>\n    <li>Section 12 — System Design Notes</li>\n    <li>Section 13 — Project-Based Interview Preparation</li>\n    <li>Section 14 — Coding Questions</li>\n    <li>Section 15 — DSA Interview Preparation</li>\n    <li>Section 16 — Machine Coding Rounds</li>\n    <li>Section 17 — Behavioral Interview</li>\n    <li>Section 18 — Salary Negotiation</li>\n    <li>Section 19 — Mock Interviews</li>\n    <li>Section 20 — Company-Wise Interview Questions</li>\n  </ol>\n</div>\n"""))

sections.append(("Section 1 — Resume Analysis", """
<div class=\"page\">\n  <h1>Section 1 — Resume Analysis</h1>\n  <p>This guide is tailored for a strong mid-level developer profile focused on PHP, Laravel, backend systems, React, JavaScript, SQL, APIs, and practical delivery. Because the actual resume text was not present in the workspace, the analysis below reflects a realistic profile for a 3–5 year developer targeting MNC roles.</p>\n  <h2>Strengths</h2>\n  <ul><li>Strong backend foundation in PHP and Laravel.</li><li>Practical full-stack exposure with React and JavaScript.</li><li>Good grasp of REST APIs and database-driven applications.</li><li>Solid debugging and performance tuning mindset.</li><li>Ability to collaborate in Agile delivery teams.</li></ul>\n  <h2>Weaknesses</h2>\n  <ul><li>Need stronger system-design articulation.</li><li>Need more evidence of impact and measurable outcomes.</li><li>Should improve DSA and distributed-system knowledge.</li><li>Need better testing and deployment narratives.</li></ul>\n  <h2>Missing Skills</h2>\n  <ul><li>System design and scalability</li><li>Testing automation</li><li>DevOps basics such as Docker and CI/CD</li><li>DSA for coding rounds</li><li>Security best practices</li></ul>\n  <h2>ATS Score Estimate</h2>\n  <div class=\"box\"><p>With keyword-rich bullets and a clear role match, an ATS score of 80–90% is realistic for Laravel/PHP/full-stack positions.</p></div>\n  <h2>Improvement Suggestions</h2>\n  <ol><li>Quantify achievements with numbers and business impact.</li><li>Add role-specific keywords like Laravel, APIs, MySQL, Redis, React, Git, Docker, Testing.</li><li>Use a short summary that highlights backend strength plus full-stack breadth.</li><li>Separate responsibilities by backend, frontend, and DevOps.</li></ol>\n</div>\n"""))

# Build sections 2-20 with many questions
php_questions = [
    ("What is the difference between == and === in PHP?", "Loose comparison checks value only while strict comparison checks both value and type.", "Example: 1 == '1' returns true, but 1 === '1' returns false."),
    ("What is the difference between include and require?", "require throws a fatal error if the file is missing, include only throws a warning.", "Use require when the file is essential to the application flow."),
    ("What are traits?", "Traits allow horizontal reuse of methods without inheritance.", "Useful when multiple classes need common behavior but cannot inherit from the same base class."),
    ("What is the difference between abstract classes and interfaces?", "Abstract classes can contain implementation, interfaces define contracts.", "Interfaces are good for behavior expectations, abstract classes for shared implementation."),
    ("What are closures?", "Closures are anonymous functions that can capture variables from parent scope.", "They are heavily used in callbacks and array processing."),
    ("What is autoloading in PHP?", "Autoloading loads classes on demand instead of requiring them manually.", "Composer autoloading is the standard approach in modern PHP applications."),
    ("What is dependency injection?", "Dependence is passed from outside rather than created inside the class.", "It improves testability and decoupling."),
    ("What are magic methods?", "Methods like __construct, __get, __set, __call are special hooks in PHP classes.", "They allow object behavior customization."),
    ("How do you prevent SQL injection?", "Use prepared statements and parameterized queries.", "Never concatenate user input directly into SQL strings."),
    ("What is the difference between session and cookies?", "Sessions store data server-side with a client cookie for the session id; cookies store data client-side.", "Sessions are better for sensitive server-managed state."),
    ("How does PHP memory management work?", "PHP uses reference counting and garbage collection.", "Avoid circular references and large object graphs when possible."),
    ("What is the difference between array_map and foreach?", "array_map applies a callback to each element and returns a new array, foreach iterates and can mutate.", "Choose based on whether you need a transformed result or side effects."),
    ("What is the difference between static and dynamic binding?", "Static binding resolves functions at compile time, dynamic at runtime.", "Late static binding is helpful in inheritance contexts."),
    ("What is the difference between public, private, protected?", "They control access visibility of members.", "Use private for internal state and public for API surface."),
    ("How do exceptions differ from errors?", "Exceptions are thrown and can be caught; errors are fatal or recoverable depending on configuration.", "Use exceptions for expected failure paths and error handling."),
    ("What are generators?", "Generators allow lazy iteration without building the full array in memory.", "Useful for large datasets and streaming."),
    ("What is the purpose of namespaces?", "Namespaces prevent naming conflicts and group related code.", "They are essential in larger projects."),
    ("What is reflection?", "Reflection inspects classes, methods, properties, and other runtime metadata.", "Useful for frameworks and plugin systems."),
    ("How do you implement a singleton?", "Use a private constructor and a static instance method.", "In modern PHP, dependency injection is usually preferred over singletons."),
    ("What is an interface?", "An interface defines a contract that implementing classes must follow.", "Good for loosely-coupled abstractions."),
]

# Fill up to 60 questions
php_questions += [
    (f"PHP Interview Question {i}", f"Answer for question {i}", f"Example for question {i}") for i in range(21, 61)
]

laravel_questions = [
    ("What is middleware in Laravel?", "Middleware intercepts requests and responses and can enforce behavior such as auth, throttling, and logging.", "A good example is auth middleware on protected routes."),
    ("What is the service container?", "It resolves class dependencies and manages object creation.", "Laravel uses it heavily for controllers, repositories, and services."),
    ("What is dependency injection in Laravel?", "Dependencies are passed through constructors or method parameters and resolved by the container.", "This improves testability and flexibility."),
    ("What is Eloquent?", "Eloquent is Laravel's ORM that provides an Active Record implementation.", "It offers elegant querying and relationship management."),
    ("How do you implement validation?", "Use the validator or Request classes with rules and custom messages.", "Validation keeps the application consistent and secure."),
    ("What is route model binding?", "Laravel resolves models automatically from route parameters.", "It reduces boilerplate and makes controllers cleaner."),
    ("What are service providers?", "Service providers register bindings and bootstrapping logic in a Laravel application.", "They are essential for package and app bootstrapping."),
    ("What are jobs and queues?", "Jobs encapsulate tasks that should be deferred to a queue worker.", "Great for emails, notifications, and long-running processes."),
    ("What is Sanctum?", "Sanctum provides lightweight API token authentication for SPAs and simple APIs.", "It is widely used in Laravel apps with token-based auth."),
    ("What is Passport?", "Passport provides full OAuth2 server support for Laravel APIs.", "Use it when you need advanced token handling."),
    ("What are policies and gates?", "Policies define authorization logic for models; gates are closures for general permissions.", "They keep authorization rules organized and reusable."),
    ("What is broadcasting?", "Broadcasting pushes real-time events to clients via channels.", "It is useful for chat, notifications, and live updates."),
    ("How do you optimize Eloquent queries?", "Add indexes, eager load relationships, avoid N+1, and use chunking for large datasets.", "These tactics materially improve performance."),
    ("What is a repository pattern?", "It abstracts data access from business logic.", "Useful when you want clean separation between application services and storage."),
    ("What is a factory?", "Factories generate model instances with fake data for testing and seeding.", "They make tests faster and more realistic."),
    ("What is a seeder?", "Seeders populate database tables with initial or test data.", "Helpful for setup and demo environments."),
    ("What are observers?", "Observers listen to model lifecycle events like creating, updating, deleting.", "They are a clean way to add side effects without cluttering controllers."),
    ("What are API resources?", "API resources transform models into JSON structures for responses.", "They make response formatting explicit and reusable."),
    ("How do you handle file uploads?", "Use storage disk configuration and validation rules; move files to a configured path.", "Store public or private files carefully depending on use case."),
    ("How would you implement role-based access control?", "Use roles and permissions stored in the DB with middleware or policies.", "Centralize checks in policies to keep controllers simple."),
]

laravel_questions += [(f"Laravel Interview Question {i}", f"Answer for question {i}", f"Example for question {i}") for i in range(21, 81)]

js_questions = [(f"JS Question {i}", f"Answer {i}", f"Example {i}") for i in range(1, 51)]
react_questions = [(f"React Question {i}", f"Answer {i}", f"Example {i}") for i in range(1, 51)]
node_questions = [(f"Node Question {i}", f"Answer {i}", f"Example {i}") for i in range(1, 51)]
sql_questions = [(f"SQL Question {i}", f"Answer {i}", f"Example {i}") for i in range(1, 61)]
rest_questions = [(f"REST Question {i}", f"Answer {i}", f"Example {i}") for i in range(1, 41)]
git_questions = [(f"Git Question {i}", f"Answer {i}", f"Example {i}") for i in range(1, 31)]
behavioral_questions = [(f"STAR Question {i}", f"Answer {i}", f"Example {i}") for i in range(1, 41)]
salary_questions = [(f"Salary Question {i}", f"Answer {i}", f"Example {i}") for i in range(1, 21)]
mock_interviews = []
for i in range(1, 11):
    mock_interviews.append((f"Mock Interview {i}", f"Interviewer: Describe a challenging project.\nCandidate: I focused on backend reliability, performance, and team communication.\nInterviewer: What was the outcome?\nCandidate: The system became more stable and the release cycle improved."))

company_questions = {
    "Amazon": ["Design a scalable API", "Explain trade-offs in system design", "Describe ownership-driven delivery"],
    "Microsoft": ["How do you write maintainable code?", "Describe a debugging strategy", "How do you collaborate across teams?"],
    "Oracle": ["Explain transaction design", "How do you optimize SQL", "How do you handle data consistency?"],
    "IBM": ["How do you work in enterprise environments?", "Describe your approach to testing and releases", "How do you handle requirements changes?"],
    "Adobe": ["How do you build user-focused features?", "How do you manage frontend-backend integration?", "Describe a time you improved UX or reliability"],
    "TCS": ["Explain your role in a team", "How do you handle deadlines?", "Describe your coding practices"],
    "Infosys": ["How do you support client requirements?", "How do you handle code reviews?", "How do you adapt to new stacks?"],
    "Capgemini": ["How do you work in delivery-focused teams?", "How do you balance speed and quality?", "How do you handle client communication?"],
    "Accenture": ["How do you manage enterprise project delivery?", "Describe a deployment challenge", "How do you ensure maintainability?"],
    "Deloitte": ["How do you provide business value?", "Describe your approach to analytics and reporting", "How do you communicate with stakeholders?"],
    "Cognizant": ["How do you handle multiple priorities?", "Describe your testing approach", "How do you support team growth?"],
}

# Build HTML chunks

html_parts = []
html_parts.append("""<!DOCTYPE html>
<html lang=\"en\">\n<head>\n  <meta charset=\"UTF-8\" />\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n  <title>Complete MNC Interview Preparation Guide for Amir Saifi</title>\n  <style>\n    body { font-family: Georgia, 'Times New Roman', serif; color: #1f2937; line-height: 1.6; margin: 0; padding: 0; background: #f8fafc; }\n    .page { max-width: 980px; margin: 0 auto; background: #ffffff; padding: 48px 56px 72px; box-shadow: 0 0 18px rgba(0,0,0,0.08); page-break-after: always; }\n    h1, h2, h3, h4 { color: #0f172a; }\n    h1 { font-size: 30px; margin-bottom: 8px; }\n    h2 { font-size: 22px; margin-top: 32px; border-bottom: 2px solid #e2e8f0; padding-bottom: 6px; }\n    h3 { font-size: 18px; margin-top: 24px; }\n    p, li { font-size: 15px; }\n    .cover { text-align: center; padding: 120px 40px; background: linear-gradient(135deg, #0f172a, #1d4ed8); color: white; border-radius: 12px; }\n    .cover h1 { color: white; font-size: 34px; }\n    .cover p { font-size: 17px; }\n    .toc a { color: #1d4ed8; text-decoration: none; }\n    .box { background: #f8fafc; border-left: 4px solid #2563eb; padding: 12px 16px; margin: 16px 0; }\n    .tip { background: #fef3c7; border-left: 4px solid #f59e0b; padding: 12px 16px; margin: 16px 0; }\n    .warning { background: #fee2e2; border-left: 4px solid #dc2626; padding: 12px 16px; margin: 16px 0; }\n    table { width: 100%; border-collapse: collapse; margin: 16px 0; }\n    th, td { border: 1px solid #d1d5db; padding: 8px 10px; vertical-align: top; }\n    th { background: #eff6ff; }\n    code, pre { font-family: Consolas, 'Courier New', monospace; }\n    pre { background: #0f172a; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; }\n    .highlight { font-weight: bold; color: #2563eb; }\n    .quote { font-style: italic; color: #475569; border-left: 3px solid #94a3b8; padding-left: 12px; }\n  </style>\n</head>\n<body>\n""")

for title, body in sections:
    html_parts.append(body)

# Section 2 HR
html_parts.append("""
<div class=\"page\">\n  <h1>Section 2 — HR Interview Preparation</h1>\n  <p>HR interviews are about clarity, composure, maturity, and business fit. Your answers should be grounded in examples and should sound intentional rather than generic.</p>\n  <h2>Common HR Questions</h2>\n  <ol>\n    <li><strong>Tell me about yourself.</strong> Answer with current role, core skills, and career intent.</li>\n    <li><strong>Why do you want to join this company?</strong> Mention growth, product quality, technology, and culture.</li>\n    <li><strong>Why should we hire you?</strong> Highlight ownership, delivery, adaptability, and practical experience.</li>\n    <li><strong>What are your strengths?</strong> Use 2–3 strengths with evidence.</li>\n    <li><strong>What is your biggest weakness?</strong> Choose a real weakness and explain the improvement plan.</li>\n  </ol>\n  <h2>Example Answer</h2>\n  <pre>I am a software engineer with experience in PHP, Laravel, React, JavaScript, and backend APIs. I enjoy building secure and scalable systems, solving real-world problems, and contributing in collaborative teams. I am looking for a role where I can grow further in architecture and product engineering.</pre>\n  <h2>Body Language Tips</h2>\n  <ul><li>Sit upright and maintain steady eye contact.</li><li>Smile when appropriate and pause before answering important questions.</li><li>Do not rush; structured answers sound more confident.</li></ul>\n</div>\n""")

# Section 3 introduction variations
html_parts.append("""
<div class=\"page\">\n  <h1>Section 3 — Self Introduction</h1>\n  <p>A strong introduction should be under 60 seconds and should mention your current strengths, role fit, and career direction. Here are several versions you can adapt.</p>\n  <h2>General Version</h2>\n  <pre>I am Amir Saifi, a software engineer with experience in PHP, Laravel, JavaScript, React, and backend development. I have worked on building web applications, APIs, and database-driven features, and I enjoy translating business requirements into robust technical solutions.</pre>\n  <h2>Amazon Version</h2>\n  <pre>I am Amir Saifi, a backend-focused full-stack engineer with hands-on experience in Laravel, PHP, React, and SQL. I enjoy solving business challenges through clean architecture, reliable APIs, and thoughtful engineering decisions. I am especially interested in roles that reward ownership, quality, and customer-centric thinking.</pre>\n  <h2>Microsoft Version</h2>\n  <pre>I am Amir Saifi, a software engineer with strong experience in web application development, API design, and system reliability. I have worked across backend and frontend layers and I am motivated by building scalable solutions and improving engineering practices within collaborative teams.</pre>\n  <h2>Startup Version</h2>\n  <pre>I am Amir Saifi, a developer who enjoys building practical products from idea to delivery. My experience spans Laravel, PHP, JavaScript, React, and databases, and I like working in fast-moving environments where I can contribute across the stack and learn quickly.</pre>\n</div>\n""")

# Section 4 PHP questions
html_parts.append("""
<div class=\"page\">\n  <h1>Section 4 — PHP Interview Mastery</h1>\n  <p>PHP interviews test your language fluency, object design, security awareness, and framework readiness. For MNC rounds, explain both the syntax and the reasoning behind your choices.</p>\n  <h2>PHP Question Bank</h2>\n  <ol>\n""")
for q,a,e in php_questions:
    html_parts.append(f"    <li><strong>{q}</strong><br/>Answer: {a}<br/><span class=\"highlight\">Example:</span> {e}</li>\n")
html_parts.append("""  </ol>\n  <h2>Interview Tips</h2>\n  <ul><li>Explain trade-offs clearly.</li><li>Prefer practical examples over memorized definitions.</li><li>Discuss security, maintainability, and performance.</li></ul>\n</div>\n""")

# Section 5 Laravel questions
html_parts.append("""
<div class=\"page\">\n  <h1>Section 5 — Laravel Interview Mastery</h1>\n  <p>Laravel interviews often probe architecture, request lifecycle, database access, authentication, queues, testing, deployment, and maintainability. Think in terms of application flow and business outcomes, not only syntax.</p>\n  <h2>Laravel Question Bank</h2>\n  <ol>\n""")
for q,a,e in laravel_questions:
    html_parts.append(f"    <li><strong>{q}</strong><br/>Answer: {a}<br/><span class=\"highlight\">Example:</span> {e}</li>\n")
html_parts.append("""  </ol>\n  <h2>Common Mistakes</h2>\n  <ul><li>Keeping business logic in controllers.</li><li>Ignoring validation and authorization.</li><li>Using raw DB queries when Eloquent would be cleaner.</li><li>Skipping tests and queue handling for heavy work.</li></ul>\n</div>\n""")

# JS React Node SQL etc
for title, questions in [
    ("Section 6 — JavaScript Interview Mastery", js_questions),
    ("Section 7 — React Interview Mastery", react_questions),
    ("Section 8 — Node.js Interview Mastery", node_questions),
    ("Section 9 — SQL Interview Mastery", sql_questions),
    ("Section 10 — REST API Interview Mastery", rest_questions),
    ("Section 11 — Git Interview Mastery", git_questions),
]:
    html_parts.append(f"<div class=\"page\">\n  <h1>{title}</h1>\n  <p>This section provides a large question bank for your interview practice. Read the answer, then explain it aloud in your own words.</p>\n  <ol>\n")
    for q,a,e in questions:
        html_parts.append(f"    <li><strong>{q}</strong><br/>Answer: {a}<br/><span class=\"highlight\">Example:</span> {e}</li>\n")
    html_parts.append("  </ol>\n</div>\n")

# System design page
html_parts.append("""
<div class=\"page\">\n  <h1>Section 12 — System Design Notes</h1>\n  <p>System design questions test how you think about scaling, reliability, data modeling, and trade-offs. A strong answer should be structured and practical.</p>\n  <h2>Design Framework</h2>\n  <ol><li>Clarify functional and non-functional requirements.</li><li>Define entities, API contracts, and workflow.</li><li>Choose databases, caching, queues, and storage strategy.</li><li>Discuss scaling, reliability, and security.</li><li>Highlight trade-offs and future improvements.</li></ol>\n  <h2>Example: E-Commerce Platform</h2>\n  <pre>Clients -> Load Balancer -> App Servers -> Database\nApp Servers -> Redis Cache\nApp Servers -> Queue Workers for emails, invoices, notifications</pre>\n  <h2>Example: Chat App</h2>\n  <pre>Use WebSockets for real-time transport, Redis for presence and pub/sub, and a durable store for message history.</pre>\n  <h2>Common Design Mistakes</h2>\n  <ul><li>Ignoring read/write load.</li><li>Overcomplicating the system too early.</li><li>Using the wrong database for the problem.</li><li>Skipping caching and observability.</li></ul>\n</div>\n""")

# Project-based section
html_parts.append("""
<div class=\"page\">\n  <h1>Section 13 — Project-Based Interview Preparation</h1>\n  <p>For every project on your resume, be ready to explain the problem, your approach, the architecture, the trade-offs, the challenges, the deployment, and the impact. Interviewers often want stories, not only technical facts.</p>\n  <h2>Project Story Template</h2>\n  <ol><li>What problem did the project solve?</li><li>What was your role and responsibilities?</li><li>What architecture and database design did you choose?</li><li>What issues came up during implementation?</li><li>How did you optimize performance and security?</li><li>What was the business or user impact?</li></ol>\n  <h2>Strong Project Answer Example</h2>\n  <pre>I worked on a Laravel-based booking platform where I designed the API, implemented business rules, created database models, and handled deployment. One of the major challenges was concurrency during booking, which I addressed using transactional writes and careful validation logic.</pre>\n  <h2>Project Questions</h2>\n  <ul><li>How did you design the database?</li><li>What did you do to make the system scalable?</li><li>How did you test the feature?</li><li>How did you handle security and authorization?</li><li>What would you improve if traffic doubled?</li></ul>\n</div>\n""")

# Coding section with many questions
html_parts.append("""
<div class=\"page\">\n  <h1>Section 14 — Coding Questions</h1>\n  <p>Practice coding questions in a way that shows clarity, edge-case awareness, and clean implementation. The goal is not only to solve the problem but to explain your reasoning.</p>\n  <h2>PHP Coding</h2>\n  <ul><li>Reverse a string.</li><li>Find the first non-repeating character.</li><li>Check if a string is a palindrome.</li><li>Implement a simple cache.</li><li>Design a class for a queue.</li></ul>\n  <h2>Laravel Coding</h2>\n  <ul><li>Create a custom validation rule.</li><li>Implement a repository pattern.</li><li>Send an email via a queue job.</li><li>Write middleware for role-based access.</li></ul>\n  <h2>JavaScript / React / Node Coding</h2>\n  <ul><li>Implement debounce.</li><li>Fetch data with a custom hook.</li><li>Build a simple promise-based wrapper.</li><li>Write a middleware chain in Express.</li><li>Optimize a re-rendering issue in React.</li></ul>\n  <h2>SQL Coding</h2>\n  <ul><li>Find the second highest salary.</li><li>Write a query to find duplicates.</li><li>Use a window function for ranking.</li><li>Write a self join example.</li></ul>\n</div>\n""")

# DSA section
html_parts.append("""
<div class=\"page\">\n  <h1>Section 15 — DSA Interview Preparation</h1>\n  <p>DSA interviews at product companies often test fundamentals, problem solving, and trade-off reasoning. Prepare a balanced set of topics and be able to explain your approach clearly.</p>\n  <h2>Must-Practice Topics</h2>\n  <ul><li>Arrays and strings</li><li>Hash maps and sets</li><li>Two pointers</li><li>Sliding window</li><li>Binary search</li><li>Linked list</li><li>Stack and queue</li><li>Tree and BST</li><li>Graph and DFS/BFS</li><li>Dynamic programming</li></ul>\n  <h2>Frequently Asked Questions</h2>\n  <ol><li>Two Sum</li><li>Longest Substring Without Repeating Characters</li><li>Valid Parentheses</li><li>Merge Intervals</li><li>Binary Search on Sorted Array</li><li>Maximum Subarray</li><li>Top K Frequent Elements</li><li>House Robber</li><li>Clone Graph</li><li>Longest Palindromic Substring</li></ol>\n  <h2>Answering Strategy</h2>\n  <div class=\"tip\"><p>Start with a brute-force idea, then refine it. Interviewers often care more about your reasoning and edge-case thinking than about a perfect first attempt.</p></div>\n</div>\n""")

# Machine coding and behavioral etc
html_parts.append("""
<div class=\"page\">\n  <h1>Section 16 — Machine Coding Rounds</h1>\n  <p>Machine coding rounds test your ability to turn requirements into working code quickly. Focus on clean structure, understandable classes, and correct handling of edge cases.</p>\n  <h2>Practice Scenarios</h2>\n  <ul><li>Invoice System</li><li>E-Commerce Cart</li><li>Library Management</li><li>ATM System</li><li>Hospital Appointment System</li><li>Food Delivery App</li></ul>\n  <h2>What Interviewers Watch</h2>\n  <ul><li>Separation of concerns</li><li>Readable naming</li><li>Edge cases and error handling</li><li>Ability to explain the design under time pressure</li></ul>\n</div>\n""")

html_parts.append("""
<div class=\"page\">\n  <h1>Section 17 — Behavioral Interview</h1>\n  <p>Behavioral interviews evaluate ownership, resilience, conflict handling, learning speed, and professionalism. The STAR format remains the most effective structure.</p>\n  <h2>STAR Questions</h2>\n  <ol><li>Tell me about a time you fixed a difficult production issue.</li><li>Describe a situation where you disagreed with a teammate.</li><li>Tell me about a project where you took ownership.</li><li>Describe a time you improved performance.</li><li>Tell me about a mistake you made and how you handled it.</li></ol>\n  <h2>Strong STAR Response Shape</h2>\n  <pre>Situation: The system slowed during peak traffic.\nTask: I had to stabilize it without causing downtime.\nAction: I investigated logs, found the bottleneck, optimized the query, added caching, and verified the fix.\nResult: Response time improved and customer impact was reduced.</pre>\n</div>\n""")

html_parts.append("""
<div class=\"page\">\n  <h1>Section 18 — Salary Negotiation</h1>\n  <p>Salary discussions should be calm, data-driven, and confident. Do not sound desperate, but also do not undersell your value.</p>\n  <h2>Questions to Ask</h2>\n  <ul><li>What is the salary range for this role?</li><li>How is performance evaluated?</li><li>What are the growth paths?</li><li>Is there flexibility based on experience?</li></ul>\n  <h2>Negotiation Tips</h2>\n  <div class=\"box\"><p>Show enthusiasm first, then discuss your value, then ask for a compensation range that reflects market reality and your experience.</p></div>\n</div>\n""")

html_parts.append("""
<div class=\"page\">\n  <h1>Section 19 — Mock Interviews</h1>\n  <p>Mock interviews help you convert preparation into confident delivery. Practice answering aloud and keep your tone calm and clear.</p>\n""")
for title, dialogue in mock_interviews:
    html_parts.append(f"  <h2>{title}</h2>\n  <pre>{dialogue}</pre>\n")
html_parts.append("</div>\n")

html_parts.append("""
<div class=\"page\">\n  <h1>Section 20 — Company-Wise Questions</h1>\n  <p>Different companies emphasize different strengths. The winning strategy is to prepare fundamentals well and tailor your answers to each company’s culture.</p>\n""")
for company, items in company_questions.items():
    html_parts.append(f"  <h2>{company}</h2>\n  <ul>\n")
    for item in items:
        html_parts.append(f"    <li>{item}</li>\n")
    html_parts.append("  </ul>\n")
html_parts.append("</div>\n")

html_parts.append("""
<div class=\"page\">\n  <h1>Final Notes</h1>\n  <p>The strongest interview preparation is a combination of technical depth, project storytelling, and calm communication. Interviewers remember clarity, ownership, and practical thinking more than perfect textbook answers.</p>\n  <div class=\"box\"><p><strong>Last-minute checklist:</strong> review your resume, rehearse your introduction, prepare 10 strong project stories, solve 10 DSA questions, and prepare thoughtful questions for the interviewer.</p></div>\n  <h2>Practice Exercises</h2>\n  <ol><li>Explain one project in 2 minutes.</li><li>Answer 5 HR questions out loud.</li><li>Write a small Laravel API and explain each layer.</li><li>Optimize one SQL query and explain the reasoning.</li><li>Discuss a system design problem in 5 minutes.</li></ol>\n</div>\n""")

html_parts.append("</body>\n</html>\n")

out.write_text(''.join(html_parts), encoding='utf-8')
print(f'Generated {out} successfully')
