# Haptic Greeting Corpus and Human Perceptions in Recognizing Haptic Greetings and Scenarios

The project aims to build a corpus of haptic greetings to develop social robots capable of performing socially meaningful touch. Following the collection of these greetings, this phase focuses on annotating egocentric videos and investigating human perception in recognizing haptic greeting types and scenarios. The results will be used to establish the human baselines for evaluating model performance. 

## How it’s conducted:

### Tech used: ELAN 6.5, Python, Qualtrics, SPSS, Excel, Microsoft Clipchamp

### Corpus Compilation

Haptic greetings are a common form of non-verbal communication, typically expressed through physical touch. These greetings often carry social and emotional meanings (Van Erp & Toet, 2015; App et al., 2011; Field, 2010). Despite the versatile functions of touch, this modality has only recently gained more attention in human-robot interaction. To perform touch when greeting, social robots must be able to automatically recognize and predict the potential of different haptic interactions across different social contexts. 

This corpus includes eight types of greetings: handshake, high five, hug, fist bump, shoulder tap, arm touch, elbow bump, and holding hands, set across four scenarios: comforting, supportive, affectionate and playful. In total, there were 21 dyads featuring both egocentric views (from both responders and initiators) and exocentric views in the corpus. In this part of the project, we focused specifically on annotating the egocentric view. 

### Annotation

The annotation focused on having information about the duration of the initiating actions, the varying timing of the touching behaviors, and the end of the greeting. Therefore, an annotation scheme was created. ELAN 6.5 was used to annotate the corpus. The annotation scheme includes one tier Responder with 3 types of vocabularies: start of greeting, first physical contact, and end of greeting. 
(See Figure 1 for an example of the annotation file)
![Screenshot of a annotation file on ELAN.](https://github.com/phamhamy122-beep/Lab1--The-Haptic-Greeting-Corpus/blob/main/Figure%201.png)
### Investigating human perceptions

In this perception study, three aspects of human perceptive capacity from the initiating phase of the greetings, which are perceiving gestures, scenarios, and time, were investigated. The result of this study will also be used as the human baselines for training the models. 

#### Research questions 

**Q1: How well do people predict accurately different types of gestures at different timeframe percentages?** To answer this research question, the approaching phase of the interactions was cut into 3 arbitrarily chosen time frame percentages: 50%, 75%, and 100% ( in the 100% timeframe, the first physical contact takes place).

**Q2: Can humans tell the differences between the 4 scenarios from the video material of the corpus?**

#### Hypotheses

The goals of the perception study are to analyze the corpus in predicting gestures and scenarios and to have human baselines. Firstly, we want to investigate the ability to perceive gestures at different timeframe percentages. Suggesting that at the lower rates of timeframes, people can still perceive gestures as well as at the higher number of timeframe rates, the researcher poses two hypotheses:

**(H1) The prediction accuracy score of the type of gesture at a higher rate of time frames is higher than the prediction score at the lower rates of time frames (accuracy score at 100% timeframes > accuracy score at 75% timeframes> accuracy score at 50% timeframes)**

**(H2) The prediction scores at 100%, 75%, and 50% timeframe rates are all higher than the chance level (the prediction accuracy scores are all higher than 12.5%).**

The second goal of the perception test is to test whether the prediction accuracy scores of all scenarios are higher than chance. The results from this perception test can help to decide if humans can tell the difference between the four types of scenarios. Therefore, the third hypothesis is that:

**(H3) The accuracy prediction scores for 4 types of scenarios are higher than chance (25%)**

To have a more insightful understanding of the perception of humans, we would like to see if the differences in expressions of the performers would affect the perception accuracy scores of the perceiver. Suggesting that the performances of people with exaggerated movements will lead to higher scores, and vice versa. Our fourth hypothesis is that:

**(H4) Performers with exaggerated movements (Dyad 1) will get higher perception accuracy scores than performers with less exaggerated movements (Dyad 10)**

#### Materials 

Egocentric videos of responders from two dyads (Dyad 1 and Dyad 10) were selected as stimuli for the perception study. These dyads were chosen based on the visibility of facial expressions in the videos and the level of movement exaggeration. Participants in Dyad 1 exhibited frequent exaggerated movements and highly expressive facial expressions, demonstrating a strong ability to interpret and act out scenarios. Conversely, Dyad 10 was selected for their sill in interpreting scenarios despite having less exaggerated movements compared to participants in Dyad 1. 

A total of 64 video clips from these two dyads were trimmed at three different timestamps: 50%, 75%, and 100% of the Start of Greeting. This resulted in 384 unique video stimuli, which were then divided randomly into 12 distinct groups. Each participant was randomly assigned to one group of videos (32 videos). After viewing each video 2 to 3 times, participants were asked to identify the scenario and greeting type that they observed.  

Find the cleaned dataset and python code in the master branch [here](https://github.com/phamhamy122-beep/Lab1--The-Haptic-Greeting-Corpus/tree/master)
Read the full report [here](https://github.com/phamhamy122-beep/Lab1--The-Haptic-Greeting-Corpus/blob/master/Lab%20Rotation%201%20Report%20-%20final%20-%20Github%20version.docx)

