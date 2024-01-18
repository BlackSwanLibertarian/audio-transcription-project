import openai

def modify_resume_for_job_description(resume_text, job_description, api_key):
    """
    Modify the professional experience in the resume to better match the job description.

    :param resume_text: A string containing the professional experience section of your resume.
    :param job_description: A string containing the job description.
    :param api_key: Your OpenAI API key.
    :return: A string with the modified professional experience.
    """
    openai.api_key = api_key

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",  # Using the specified chat model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Here is a professional experience section of a resume:\n\n" + resume_text +
                                            "\n\nAnd here is a job description:\n\n" + job_description +
                                            "\n\nRewrite the professional experience to better match the job description so that it will pass ATS."}
            ]
        )
        # Assuming the last message from the model will be the revised professional experience
        return response.choices[-1].message['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
api_key = "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"  # Replace with your actual API key
resume_text = """Ripple
Product
Management
Intern
May 2023 – Aug 2023
|
New York,
NY
•
Aided in developing an innovative roadmap for a product aggregating liquidity across cryptocurrency exchanges, collaborating with teams to refine features, address customer challenges, and align the product with market demand
•
Pioneered and executed a strategic project to optimize and migrate trading flows, significantly reducing dependence on external systems, enhancing operational efficiency, and securing monthly cost savings of $100k
•
Led user research through in-depth interviews with over 25 prospects, refining focus to a specific niche and informing strategic decisions to optimize product relevance and market penetration for target customer segments
•
Evaluated and refined processes for a new B2B2C product, focusing on strengthening fraud detection, KYC, and transaction monitoring, to inform pivotal build vs partner decisions, enhancing compliance and risk mitigation
Blockchain
Triangle
(Seed
stage
startup)
MBA
Consultant
-
Product
Strategy
Mar 2023 – Apr 2023
|
Ann Arbor,
MI / Bermuda
•
Designed a blockchain-based sustainability-linked underwriting product for farmers in the Great Lakes region by gathering pertinent farm-level data across varied sources, ensuring compliance with ESG and TCFD standards
Prospa
(Y
Combinator
2021
-
$
4M
seed
stage
FinTech
startup)
Product
Manager
Feb 2022 – Jul 2022
|
Lagos,
Nigeria
•
Spearheaded the loans business, assisting the Founder/CEO in setting the strategy and overseeing the delivery of digital banking services for SMEs in Nigeria, managing $1M in annualized loans and promoting financial inclusion
•
Formulated and executed a product-led go-to-market strategy, leveraging application usage metrics to target specific customer cohorts, which resulted in a 25% month-over-month increase in first-time loans acquisition from customers
•
Influenced engineering & design teams, crafting comprehensive product documents, prioritizing the backlog, designing wireframes, and implementing agile sprints, which collectively drove a 75% monthly surge in loan volume
•
Designed and implemented advanced credit scoring algorithms and automation tactics to enhance repayment rates, yielding a 15% reduction in defaults and a 50% augmentation in customer lifetime value
One
Acre
Fund
(Social
impact
financing
for
farmers)
Senior
Program
Associate
(Product
Manager
equivalent)
Oct 2019 – Jan 2022
|
Muramvya,
Burundi
•
Oversaw a 500-member field team in delivering financing, distributing agricultural inputs, and providing training to 150,000 underserved farmers, elevating their annual ROI by 30% and fostering sustainable agricultural practices
•
Conceived and realized a mobile money repayment solution by leading product and engineering teams, addressing significant inconveniences for farmers and enhancing Net Promoter Score (NPS) by 35%
•
Initiated and deployed a mobile-first customer acquisition strategy and digital marketplace for agricultural inputs, elevating per-customer purchases by 30% and optimizing operating costs by 40%
•
Instilled a data-centric organizational culture by establishing weekly KPIs and disseminating analytical dashboards, achieving approximately 99% loan repayment collection on a $13M annual lending portfolio
J.P.
Morgan
Analyst
-
Investment
Banking
Jul 2016 – Oct 2019
Mumbai,
India / Hong Kong
•
Crafted a compelling investment memorandum and business plan, and articulated a persuasive pitch to venture capitalists for an Indian online logistics marketplace, successfully securing $100M in funding at a $1B valuation
•
Developed intricate financial and operating models, facilitated negotiations, and delivered presentations to the board of a prominent Indian conglomerate, culminating in the successful execution of an $830M spin-off transaction
•
Evaluated opportunities in convertible and exchangeable bond financing for companies across the Asia Pacific from the Hong Kong desk, successfully closing seven transactions totaling $5B in value"""
job_description = """"Job Description:

Remitly is on a mission to transform the lives of immigrants and their families by providing the most trusted financial products and services on the planet. Since 2011, we have been tirelessly delivering on our promises to immigrants sending their hard earned money home. Today, we are reimagining international payments at scale and building new products to create deeper relationships with our customers and their loved ones across the globe. Join over 2,700 employees across 10 offices who are growing their careers while having a positive impact on people globally.

Remitly is registered as a Money Services Business in the U.S., Canada, EU, United Kingdom, Singapore and Australia. Each of these jurisdictions require, among other items, that Remitly maintain a comprehensive Risk and Compliance Program.

About the Role:

We are looking for an outstanding candidate for the Senior Product Manager role within the Global Money Movement (GMM) team at Remitly. The Global Money Movement (GMM) Team is focused on enabling new payment options and improving the existing payments experience for our customers sending from 30 countries to our over 170 receive countries. The GMM team plays a crucial role in driving Remitly's ability to connect with international customers and offer a diverse range of Pay-in and Pay-out methods, including cards, bank transfers, and alternative payment methods.

As a Senior Product Manager on the Global Money Movement (GMM) team, you will partner with engineers, designers, marketers, finance, legal, business development and other product managers to create product experiences that deliver exponential value to our customers, globally. You will report to the Group Product Manager, Payments.

You Will:

Help shape Remitly's global payments product roadmap and build a prioritization framework that captures relevant tradeoffs for the team while creating organizational alignment
Leverage customer feedback, market analysis, and quantitative research to recommend and implement enhancements, enriching the payment experience for our customers.
Lead the delivery of an outstanding payments experience through development of detailed requirements, implementation plans and execution
Be a customer advocate and identify those areas that require deeper customer insights and lead research to learn more about Remitly's customers and their needs
Work with designers to define interaction, design and UI requirements and priorities
Set up and analyze A/B tests and provide comprehensive test readouts with well thought through recommendations
Understand the payment platform end to end, the APIs and dependencies, and use this knowledge to create new and improve our payment systems
Engage with stakeholders to understand customer and business needs to inform priorities, sequencing and roadmap
Stay informed about the latest developments in payments and FinTech
You Have:

8+ years of relevant experience in product management with at least 5 years experience in the payments space
Experience motivating cross-functional teams; ideally across software engineering, UI design, and analytics, with an understanding of how things work within those domains
Experience with large-scale web, e-commerce applications/mobile applications
Data is the source of your decision-making and you will have experience working with customer data to develop better customer experiences
Experience setting and implementing product strategy, road-mapping, and prioritization
Experience working with engineers to make tough technical tradeoffs and you can sweat the details to understand the impacts of these tradeoffs and find a careful balance between short-term outcomes and long-term effects.
Our Benefits:

Flexible paid time off
Health, dental, and vision benefits + 401k plan with company matching
Company contributions to your HSA plan, if you choose one
Employee Stock Purchase Plan (ESPP) available for eligible employees
Continuing education and corridor travel benefits"""

modified_resume = modify_resume_for_job_description(resume_text, job_description, api_key)
print(modified_resume)
