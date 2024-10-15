allAbstracts = [' Humanity is now facing what may be the biggest challenge to its existence: irreversible climate change brought about by human activity. Our planet is in a state of emergency, and we only have a short window of time (7–8 years) to enact meaningful change. The goal of this systematic literature review is to summarize the peer-reviewed literature on proposed solutions to climate change in the last 20 years (2002–2022), and to propose a framework for a unified approach to solving this climate change crisis. Solutions reviewed include a transition toward use of renewable energy resources, reduced energy consumption, rethinking the global transport sector, and nature-based solutions. This review highlights one of the most important but overlooked pieces in the puzzle of solving the climate change problem – the gradual shift to a plant-based diet and global phaseout of factory (industrialized animal) farming, the most damaging and prolific form of animal agriculture. The gradual global phaseout of industrialized animal farming can be achieved by increasingly replacing animal meat and other animal products with plant-based products, ending government subsidies for animal-based meat, dairy, and eggs, and initiating taxes on such products. Failure to act will ultimately result in a scenario of irreversible climate change with widespread famine and disease, global devastation, climate refugees, and warfare. We therefore suggest an “All Life” approach, invoking the interconnectedness of all life forms on our planet. The logistics for achieving this include a global standardization of Environmental, Social, and Governance (ESG) or similar measures and the introduction of a regulatory body for verification of such measures. These approaches will help deliver environmental and sustainability benefits for our planet far beyond an immediate reduction in global warming.', ' This paper focuses on climate anxiety and its role in the psychology of climate change, compared with responses to the COVID-19 global pandemic. Four psychological hypotheses for why we do not act on climate change will be reviewed, and the role of anxiety for each, as well as potential solutions. Different types of climate anxiety both inside and outside the clinic will be explored, along with associated defence mechanisms and treatment.', " We assess evidence relevant to Earth's equilibrium climate sensitivity per doubling of atmospheric CO2, characterized by an effective sensitivityS. This evidence includes feedback process understanding, the historical climate record, and the paleoclimate record. AnSvalue lower than 2\xa0K is difficult to reconcile with any of the three lines of evidence. The amount of cooling during the Last Glacial Maximum provides strong evidence against values ofSgreater than 4.5\xa0K. Other lines of evidence in combination also show that this is relatively unlikely. We use a Bayesian approach to produce a probability density function (PDF) forSgiven all the evidence, including tests of robustness to difficult‐to‐quantify uncertainties and different priors. The 66% range is 2.6–3.9\xa0K for our Baseline calculation and remains within 2.3–4.5\xa0K under the robustness tests; corresponding 5–95% ranges are 2.3–4.7\xa0K, bounded by 2.0–5.7\xa0K (although such high‐confidence ranges should be regarded more cautiously). This indicates a stronger constraint onSthan reported in past assessments, by lifting the low end of the range. This narrowing occurs because the three lines of evidence agree and are judged to be largely independent and because of greater confidence in understanding feedback processes and in combining evidence. We identify promising avenues for further narrowing the range inS, in particular using comprehensive models and process understanding to address limitations in the traditional forcing‐feedback paradigm for interpreting past changes.", ' This article provides a stocktake of the adaptation literature between 2013 and 2019 to better understand how adaptation responses affect risk under the particularly challenging conditions of compound climate events. Across 39 countries, 45 response types to compound hazards display anticipatory (9%), reactive (33%), and maladaptive (41%) characteristics, as well as hard (18%) and soft (68%) limits to adaptation. Low income, food insecurity, and access to institutional resources and finance are the most prominent of 23 vulnerabilities observed to negatively affect responses. Risk for food security, health, livelihoods, and economic outputs are commonly associated risks driving responses. Narrow geographical and sectoral foci of the literature highlight important conceptual, sectoral, and geographic areas for future research to better understand the way responses shape risk. When responses are integrated within climate risk assessment and management, there is greater potential to advance the urgency of response and safeguards for the most vulnerable.', ' Climate change has been shown to be directly linked to multiple physiological sequelae and to impact health consequences. However, the impact of climate change on mental health globally, particularly among vulnerable populations, is less well understood. To explore the mental health impacts of climate change in vulnerable populations globally. We performed an integrative literature review to identify published articles that addressed the research question:What are the mental health impacts of climate change among vulnerable populations globally?The Vulnerable Populations Conceptual Model served as a theoretical model during the review process and data synthesis. One hundred and four articles were selected for inclusion in this review after a comprehensive review of 1828 manuscripts. Articles were diverse in scope and populations addressed. Land-vulnerable persons (either due to occupation or geographic location), Indigenous persons, children, older adults, and climate migrants were among the vulnerable populations whose mental health was most impacted by climate change. The most prevalent mental health responses to climate change included solastalgia, suicidality, depression, anxiety/eco-anxiety, PTSD, substance use, insomnia, and behavioral disturbance. Mental health professionals including physicians, nurses, physician assistants and other healthcare providers have the opportunity to mitigate the mental health impacts of climate change among vulnerable populations through assessment, preventative education and care. An inclusive and trauma-informed response to climate-related disasters, use of validated measures of mental health, and a long-term therapeutic relationship that extends beyond the immediate consequences of climate change-related events are approaches to successful mental health care in a climate-changing world.']


keywords = ["mitigate", "climate anxiety", "climate change", "mental health", "global warming"]

for keyword in keywords: 

  for index, abstract in enumerate(allAbstracts):
      if keyword.lower() in abstract.lower():
          print(f"{keyword} is in abstract {index}")

      else: 
          print(f"{keyword} is not in abstract {index}")



