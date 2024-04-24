import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='My Webpage')

st.title('Website Lorem lpsum')
st.markdown('---')
st.write("这块写什么？")
st.markdown('---')

tab1, tab2, tab3, tab4 = st.tabs(['EDA', 'NLP', 'ML', 'Summary'])



with st.sidebar:
    st.title('Welcome to my webpage!')
    st.markdown('---')
    st.markdown('侧边栏写什么？')


with tab1:
    st.header("EDA")
    st.subheader("Business Goals")
    st.write("For our project, we propose ten questions to analyze the question: "
             "How did the repeal of Roe v. Wade change the discourse over reproductive rights on Reddit?")
    st.write("We gather submissions and comments about reproductive right on Reddit. "
             "For our analysis, we will be using a combination of subreddits that are directly related to reproductive "
             "rights, such as r/birthcontrol and r/abortion, as well as those semi-relevant, such as r/politics. "
             "We used regex search to extract only posts that are related to the discussion of abortion and "
             "reproductive rights in the latter.")

    st.subheader("Analysis Report")
    st.write("Question 1:Were there any spikes in posts volume around key events or news stories related to reproductive rights and Roe v. Wade? "
             "If so, are those changes in volume persistent or merely temporary as a response to the shock?")
    st.write("Question 2:What are the most prominent birth control and abortion concerns or questions "
             "(e.g., cost, timeline, accessibility, legality, Support/Advice, etc.) on these subreddits? "
             "Are topics related to politics a prominent one among them? "
             "If not, does it change after the event?")
    st.write("Question 3:How did the popularity and engagement of reproductive rights posts on "
             "Reddit change around the key events of the Politico leak and the SCOTUS decision? "
             "Are these changes transient or persistent?")
    st.write("Question 4:Which political persons/entities/concepts are mentioned most in posts on the select reproductive rights subreddits? "
             "How did their prominence change over time?")
    st.write("Has the Repeal generated effects beyond subreddits directly related to this topic? "
             "How has user engagement r/politics reacted in response to these events?")

    st.subheader("Answers for Question 1")

    EDA1 = Image.open('C:/Users/29729/Desktop/www/EDA1.png')
    st.image(EDA1,
             use_column_width=True
             )

    st.write("1.Most notably, we observe significant spikes in activity across all subreddits around the dates of the "
             "Politico leak in early May 2022 and the SCOTUS decision overturning Roe v. Wade in late June 2022. "
             "These sudden surges strongly suggest that the leaked draft opinion and the official ruling served as "
             "catalysts, galvanizing engagement and driving more users to discuss the topic on Reddit.")
    st.write("2.However, when examining the trends more closely, we can see that these volume changes were largely "
             "temporary reactions to the shocking news developments. After a few weeks, the post numbers gradually "
             "revert back towards their pre-event levels. This pattern aligns with the concept of an "
             "‘issue attention cycle’, where a dramatic event triggers intense short-term focus that fades as the "
             "novelty wears off and other stories emerge.")
    st.write("This pattern of change in post volume posts interesting question for later analysis. "
             "What has contributed to the short attention span for users in these specialized subreddits? "
             "If there are common traits, are those traits shared with users from a more general platform for "
             "discussions about politics? "
             "These could be potentially illuminating when added into consideration for our NLP and ML question development.")


    st.subheader("Answers for Question 2")
    st.write("First, calculate the occurrence frequency of various types of issues throughout the entire period as follows.")
    st.code('''Most prominent concerns or questions overall:
               Timeline: 51916
               Accessibility: 50249
               Support/Advice: 45517
               Legality: 31160
               Cost: 4145
               Political: 356''')
    st.write("Plot a bar chart to show the overall concerns:")
    EDA2 = Image.open('C:/Users/29729/Desktop/www/overall_concerns.png')
    st.image(EDA2,
             use_column_width=True
             )

    st.write("1.'Timeline' emerges as the most frequently discussed concern overall, with 51,916 occurrences. "
             "This suggests that people are primarily seeking information about the timelines associated with "
             "birth control methods and abortion procedures, as would be expected for these highly specialized "
             "subreddits.")
    st.write("2.'Accessibility' follows closely with 50,249 occurrences, indicating that individuals are concerned "
             "about the availability and ease of access to reproductive health services. It's worth examining whether "
             "this volumn experiences any change, both in its absolute size and relative proportion to other concerns, "
             "with the shocks of external events.")
    st.write("3.'Support/Advice' is the third most prominent concern, with 45,517 occurrences, highlighting the need "
             "for emotional support and guidance during these sensitive experiences. This rich dataset could also be "
             "potentially fruitful for further analysis in sentiment and topic models, as there could be a change in "
             "themes or general emotions for these posts.")
    st.write("Next, counting the occurrence of concerns for different periods as follows:")
    st.code('''Most prominent concerns or questions by period:

Before Politico Leak:
Timeline: 21845
Support/Advice: 18095
Accessibility: 17997
Legality: 13924
Cost: 1870
Political: 90

Between Politico Leak and SCOTUS Decision:
Timeline: 21251
Support/Advice: 17564
Accessibility: 17501
Legality: 14026
Cost: 1797
Political: 168

After SCOTUS Decision:
Timeline: 28934
Support/Advice: 28557
Accessibility: 26798
Legality: 22745
Cost: 2690
Political: 220''')

    EDA3 = Image.open('C:/Users/29729/Desktop/www/Most Prominent.png')
    st.image(EDA3,
             use_column_width=True
             )

    st.write("Filter the data based on specific conditions as shown in the following table:")
    df = pd.read_csv('C:/Users/29729/Desktop/www/concerns_by_period.csv')
    st.dataframe(df, width=1000)

    st.write("Finally, estimate the relative change for each concern over different time periods as follows:")
    st.code('''Relative changes in Between Politico Leak and SCOTUS Decision compared to the previous period:
Cost: -3.90%
Timeline: -2.72%
Accessibility: -2.76%
Legality: 0.73%
Support/Advice: -2.93%
Political: 86.67%

Relative changes in After SCOTUS Decision compared to the previous period:
Cost: 49.69%
Timeline: 36.15%
Accessibility: 53.12%
Legality: 62.16%
Support/Advice: 62.59%
Political: 30.95%''')

    EDA4 = Image.open('C:/Users/29729/Desktop/www/EDA4.png')
    st.image(EDA4,
             use_column_width=True
             )

    st.write("1.When examining the concerns across different time periods, we observe notable changes in "
             "their relative prominence. Before the Politico leak, the ranking of concerns remains similar "
             "to the overall pattern, with Timeline, Support/Advice, and Accessibility being the top three. "
             "However, after the Politico leak and the SCOTUS decision, there is a significant shift in the "
             "focus of the discourse.")
    st.write("2.Between the Politico leak and the SCOTUS decision, the relative share of discussions related to "
             "Political concerns increased by a staggering 86.67% compared to the previous period. "
             "This suggests that the leak triggered a surge in political discussions surrounding reproductive "
             "rights, as people started to anticipate the potential implications of the upcoming decision.")
    st.write("After the SCOTUS decision, the relative share of all concerns increased significantly compared "
             "to the previous period. Support/Advice saw the highest relative increase at 62.59%, "
             "followed by Legality at 62.16%, and Accessibility at 53.12%. This indicates that in the aftermath "
             "of the decision, people sought more emotional support, advice, and information about the legal and "
             "accessibility aspects of reproductive rights.")
    st.subheader("Side notes of Q2:")
    st.write("1.Interestingly, while discussions related to Political concerns had the smallest share overall, "
             "they experienced the largest relative increases throughout the events. This highlights how the Roe v. Wade "
             "developments brought the political dimension of reproductive rights to the forefront, "
             "bringing an influx of new voices to the discourse beyond just the core community regularly discussing "
             "reproductive health.")
    st.write("2.These patterns of change in volume of concerns suggest the Roe v. Wade news galvanized a much wider "
             "segment to engage in the reproductive rights conversation.")
    st.write("3.Follow-up sentiment and topic analysis could illuminate if the leak and ruling sparked more polarization "
             "and stronger negative/positive sentiment among different groups, and identify what specific issues became "
             "most central to the newly energized discourse.")
    st.write("Overall, the event clearly generated a large, sustained wave of impassioned online discussion that reshaped "
             "the digital landscape around this social political issue.")



    st.subheader("Answers for Question 3")

    EDA5 = Image.open('C:/Users/29729/Desktop/www/daily_average_scores.png')
    st.image(EDA5,
             use_column_width=True
             )

    st.write("1.Most notably, there are clear spikes in average scores coinciding with the key dates of the Politico "
             "leak in early May 2022 and the SCOTUS decision in late June 2022. This affirms our assumption that "
             "these events served as catalysts for users to participate in public debates and to upvote content as "
             "the topic took center stage in the news cycle and public discourse.")
    st.write("2.Looking at the fitted lines for each time period, we see that the average score level is elevated in "
             "the periods following the Politico leak and especially after the SCOTUS decision, relative to the "
             "pre-leak period. This confirms that overall, reproductive rights posts gained higher popularity and "
             "engagement in the wake of these major developments. The")
    st.write("3.However, within both the post-leak and post-decision periods, the fitted lines have a downward slope. "
             "This implies that while these events initially galvanized intense activity, the heightened engagement was "
             "largely transient rather than persistent over time. As the news cycle moved on and public attention shifted, "
             "interaction with reproductive rights posts on Reddit gradually subsided, though still remaining somewhat above "
             "pre-event levels.")
    st.write("3.This pattern aligns with the 'issue attention cycle' observed in public opinion research, where a focusing "
             "event triggers a surge of intense interest that then fades as the novelty passes and new topics emerge. "
             "So while the Politico leak and SCOTUS decision clearly reshaped the landscape and boosted the salience of "
             "reproductive rights conversations, maintaining engagement required continued events and evolving discussions.")
    st.subheader("Conclusions for Question 3:")

    st.write("1.These findings suggest that the Roe v. Wade developments did significantly change the nature of reproductive "
             "rights discourse on Reddit, sparking greater participation and content propagation.")
    st.write("2.However, this effect was largely tied to the focusing events themselves, with a tendency to dissipate "
             "over time absent new developments, as we have seen in Q1.")

    st.subheader("Answers for Question 4")
    st.write("As shown in the pie chart below, by filtering and summarizing variables in the dataset, the percentage "
             "distribution corresponding to each variable is visualized.")
    EDA6 = Image.open('C:/Users/29729/Desktop/www/top_10_political_terms.png')
    st.image(EDA6,
             use_column_width=True
             )

    st.write("1.The prominence of judicial-related terms ('Judge," "Court," "SCOTUS') throughout the timeline "
             "highlights the centrality of legal proceedings and the judiciary in the reproductive rights discourse on Reddit.")
    st.write("2.The terms associated with political leanings ('Conservative," "Liberal') suggest that the "
             "conversation is not only about the legal aspects but also deeply entwined with political ideologies.")
    st.write("3.The peaks and troughs in the mentions of these terms align with the significant event -- Politico leakage "
             "and SCOTUS decision -- which has acted as catalysts for increased public engagement and discourse on "
             "reproductive rights on Reddit. It demonstrates how external events can influence and shape online discourse.")
    st.write("4.The persistence of certain terms over time, even after the a fair amount of weeks post ruling, indicates "
             "continued concern and discussion about the implications of the Court's decision on reproductive rights.")
    EDA7 = Image.open('C:/Users/29729/Desktop/www/smoothed_weekly_10_pol_terms.png')
    st.image(EDA7,
             use_column_width=True
             )

    st.subheader("Answers for Question 5")
    EDA8 = Image.open('C:/Users/29729/Desktop/www/pol_subs_vol_change.png')
    st.image(EDA8,
             use_column_width=True
             )

    st.write("There are clear spikes around the Politico leak and SCOTUS decision, as would be expected."
             "However, those sudden rushes are followed by a gradual decline, aligning with the 'issue attention cycle'. "
             "The downward trends of the lines after each event suggest the heightened activity was largely transient, "
             "with interest fading as the novelty wore off.")
    st.subheader("Examine the change in Engagement Metrics (Q5)")
    EDA9 = Image.open('C:/Users/29729/Desktop/www/daily_average_scores_politics.png')
    st.image(EDA9,
             use_column_width=True
             )

    st.write("1.When comparing this plot to previous plots from Q3, it shows some intriguing divergence -- while "
             "we still see post volume spikes around the key events, the overall trend is more sustained compared "
             "to previous plots. The fitted lines have slight upward slopes in the later periods, hinting at a more "
             "persistent shift in engagement and participation.")
    st.write("2.This contrast raises interesting questions about why reproductive rights discourse in r/politics exhibited greater longevity post-repeal. A few potential factors could be at play:")
    st.write("(1)Political Polarization: The plot for r/politics exhibits sharper spikes and dips, suggesting the "
             "repeal generated some individual posts that really resonated and went viral within the community. "
             "This pattern could reflect r/politics users' heightened emotional investment and polarization around "
             "such a charged political topic.")
    st.write("(2)Evolving political implications: The overturning of Roe v. Wade was not just a singular event, but also "
             "a catalyst for a complex chain reaction of political and legal developments. As states rushed to enact new "
             "laws either protecting or restricting abortion access, the issue quickly became entangled with broader debates "
             "over healthcare, civil liberties, federalism, and the role of the courts. For users in a general political "
             "discussion forum like r/politics, these secondary implications may have kept the topic of reproductive rights "
             "more consistently relevant and engaging, even as the initial shock of the repeal faded.")
    st.write("(3)Data filtering: The regex-based filtering we used to identify relevant posts in r/politics could potentially "
             "capture a broader set of tangentially related content (e.g., discussions of politicians, parties, or ideologies "
             "tied to the issue). This more expansive scope might contribute to the appearance of sustained activity compared "
             "to the narrower post criteria in the specialized subreddits.")

    st.subheader("Conclusive notes for Q5:")
    st.write("1.These findings tie back to our central research question by illuminating how external political events can "
             "rapidly reshape the landscape and intensity of reproductive rights discourse online, at least temporarily. "
             "The volatility highlights the reactive nature of much of this discussion, with key developments like the leak "
             "and ruling serving as flashpoints that suddenly mobilize engagement.")
    st.write("2.At the same time, the different patterns between specialized and general subreddits suggest that the "
             "event-driven attention dynamics can vary based on the community and audience. Further analysis of the content, "
             "sentiment, and user characteristics of these posts could help clarify how the leak and decision impacted the "
             "substance of the conversations across diverse groups.")
    st.write("3.By potentially touching on the secondary political questions and consequences, the Roe v. Wade repeal likely "
             "generated a more expansive and multifaceted discourse in r/politics that extended beyond just the core topic "
             "of abortion itself. This dynamic highlights how a major political event's impact on online discourse can "
             "reverberate far beyond its immediate flashpoint. As the ripple effects unfold across the political and legal "
             "landscape, they can generate secondary points of discussion and debate that keep users invested in the "
             "overarching issue, even as the initial surge of attention subsides.")
    st.write("4.For our research, accounting for these secondary dimensions can provide a more comprehensive understanding "
             "of how the Roe v. Wade repeal reshaped the digital conversation. By looking beyond just the immediate "
             "event-related spikes to consider the more diffuse and sustained engagement with related political questions, "
             "we can better capture the full scope and duration of the repeal's discursive impact.")

with tab2:
    st.header("NLP")
    st.subheader("Executive Summary")
    st.write("Our NLP project focused on analyzing the discussion trends in the r/birthcontrol and r/abortion subreddits,"
             " especially during the 6 months period before, during, and after the Supreme Court’s Roe v. "
             "Wade Overturn (from 03/01/2022 to 08/31/2022). "
             "This approach enables us to gain valuable insights into the domain popular terms, "
             "the prevailing topics of the time, and the sentiments of the users during this supposedly tested period. "
             "Thanks to a diverse and rigorous arsenal of tools and packages, "
             "we were able to identify several key themes of the discourse over reproductive rights on Reddit, "
             "their nuances and variation over time, and their changing moods after key events.")
    st.write("More specifically, we found additional evidence to our original hypothesis that the key "
             "political events did sour the mood of the discourse, yet not by much, and not for long.")
    st.write("In sum, these insights can be greatly useful to the works of medical experts, "
             "activists, social researchers, and policymakers, "
             "who would gain a better understanding of the public sentiment regarding such a prominent and politically charged subject.")
    st.markdown('---')

    st.subheader("Analysis Report")
    st.write("To recap, for this NLP project, we have three main business questions:")
    st.write("Question 6: What were the most frequent terms and phrases used in discussions of reproductive rights before vs. after? "
             "Reflecting the evolving discourse on this forum, how does the list of most frequent words change over time?")
    st.write("Question 7: Explore the most prominent topics and themes discussed within the reproductive rights discourse on Reddit. "
             "How does the result stack up against our custom list of concerns previously created? "
             "Are there any changes in the major themes around key events?")
    st.write("Question 8: Analyze the sentiment trends surrounding the discourse before and after the repeal of Roe v. Wade. "
             "Looking more closely, are there particular birth control or abortion procedures/aspects/concepts "
             "that are associated with more negative sentiments among subreddit users? "
             "What about the political posts/comments specifically?")


    st.subheader("Preprocessing pipeline")

    st.write("We used jonsnowlabs’ sparkNLP to create a pipeline to clean our text data. It includes the following operations:")
    st.write("DocumentAssembler(): transforms input data into Spark NLP annotated documents.")
    st.write("Tokenizer(): splits the text into individual words, also known as tokens.")
    st.write("Normalizer(): performs various text normalization techniques, such as converting text to lowercase, "
             "removing special characters, and replacing abbreviations with their full forms.")
    st.write("StopWordsCleaner(): removes common stop words from the text, such as “the”, “and”, “a”, etc., "
             "in addition to a custom list of more topic general words, "
             "which are generally not helpful in some parts of our analysis.")
    st.write("LemmatizerModel: reduces each word to its base form (lemma), "
             "which can improve the consistency of analysis by grouping together related words.")
    st.write("Finisher(): extracts the processed text from the Spark NLP document and formats it as a regular string for further analysis.")


    st.subheader("TF-IDF")
    st.write("The top 20 terms (based on their TF-IDF scores) among the submissions, and the comments, "
             "are presented in the respective tables below:")
    image1 = Image.open('C:/Users/29729/Desktop/www/score1.png')
    st.image(image1,
             caption='Table 1: Top 20 Terms in the Submissions (by TF-IDF Score)',
             use_column_width=True
             )
    image2 = Image.open('C:/Users/29729/Desktop/www/score2.png')
    st.image(image2,
             caption='Table 2: Top 20 Terms in the Comments (by TF-DF Score)',
             use_column_width=True
             )
    st.write("Among the most important words, we identify a wide range of medical terms such as ‘ultrasound’, ‘clinic’, ‘antibiotic’, ‘egg’, ‘insurance’, etc., "
             "and general identification terms such as ‘mom’, ‘country’, ‘information’, ‘choice’, ‘share’, ‘job’, etc. "
             "which are just as relevant to the domain of interest.")
    st.write("In addition, we also have the frequent word counts below where we just identify the most common words. Understandably, "
             "these words compose the general linguistic skeletons to the posts that we analyze, thus carrying less specific meanings. "
             "Notable common words include ‘pill’, ‘period’, ‘iud’, ‘time’, "
             "which are all crucial to the discourse of reproductive rights.")

    image3 = Image.open('C:/Users/29729/Desktop/www/score3.png')
    st.image(image3,
             caption='Table 3: 10 Most Common Terms in Submissions',
             use_column_width=True
             )
    image4 = Image.open('C:/Users/29729/Desktop/www/score4.png')
    st.image(image4,
             caption='Table 4: 10 Most Common Terms in Comments',
             use_column_width=True
             )

    st.subheader("What were the most frequent terms and phrases used in discussions of reproductive rights before vs. after?")
    st.write("Below, extending from our word count technique above, we have two graphs that show the frequencies of most common single words, "
             "and most common bigrams (i.e. pair of two words), respectively. "
             "The axes correspond to the frequency range post-repeal and pre-repeal, "
             "and the diagonal line serve as the balance between the two periods. "
             "In essence, words and bigrams that fall closely on the diagonal line had little frequency change between the periods. "
             "Interestingly, the bigram ‘feel well’ falls below the line, indicating a drop in frequency after the repeal, "
             "potentially signalling a reduction in general well-being of the users.")


    image5 = Image.open('C:/Users/29729/Desktop/www/word_frequency_plot.png')
    st.image(image5,
             use_column_width=True
             )
    image6 = Image.open('C:/Users/29729/Desktop/www/bigram_frequency_plot.png')
    st.image(image6,
             use_column_width=True
             )

    st.subheader("Explore the most prominent topics and themes discussed within "
                 "the reproductive rights discourse on Reddit")
    st.write("Using a Latent Dirichlet Allocation (LDA) model, we discover a set of 8 underlying topics as displayed below. "
             "Based on the component words, we qualitatively interpret these topics using reviewed literature and domain knowledge. "
             "Interestingly, abortion accessibility and clinic location and state-related help was found to be a distinct topic, "
             "which is consistent with our initial concern with increased restrictions over reprodutive rights.")
    image7 = Image.open('C:/Users/29729/Desktop/www/score7.png')
    st.image(image7,
             caption='Table 5:Topics, Components, and Interpretations',
             use_column_width=True
             )

    st.subheader("Analyze the sentiment trends surrounding the discourse before and after the repeal of Roe v. Wade")
    st.write("Using a pretrained model from SparkNLP, we aggregate and calculate the positive, "
             "negative, and neutral sentiments across 6 different component concerns that we initially specified. "
             "These concerns are Timeline, Accessibility, Legality, Support/Advice, Cost, and Political. "
             "From the table below, we see that political posts, "
             "though accounting for a very small portion of the discourse, have the largest proportion of negativity.")
    image8 = Image.open('C:/Users/29729/Desktop/www/score8.png')
    st.image(image8,
             caption='Table 6: Sentiment Components by each Concern in the Subreddits',
             use_column_width=True
             )
    st.write("Furthermore, we built another model, this time using a Valence Aware Dictionary and sEntiment Reasoner (VADER) approach. "
             "Taking advantage of the numerical nuances of this approach, we can produce a more precise measure of sentiment. "
             "Below, we calculate the overall sentiment score of the subreddits and plot it over time (the higher the sentiment score, the more positive). "
             "COnsistent with what we have previously found, the overall sentiment experienced notable drops after the two main events of the "
             "corpus leak in May 2022, and the official Overturn in June 2022.")

    image9 = Image.open('C:/Users/29729/Desktop/www/sentiment_vader_overall.png')
    st.image(image9,
             use_column_width=True
             )
    st.write("Next, we ran the same model but with each of the six concerns. Below, "
             "we can see that the previously identified ‘mood drops’ now mostly occured to the political posts. "
             "Meanwhile, posts about Cost, or Support/Advice, experienced negligible drops. "
             "Thus, we may deduce that the sour in sentiment of the subreddits can be mainly attributed to the political segment of the discourse.")

    image10 = Image.open('C:/Users/29729/Desktop/www/sentiment_vader_concerns.png')
    st.image(image10,
             use_column_width=True
             )

with tab3:
    st.header("ML")


with tab4:
    st.header("Summary")
