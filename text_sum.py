from transformers import pipeline
# summarizer = pipeline("summarization", model="knkarthick/MEETING_SUMMARY", truncation = True)
text = '''
Das : Hi and welcome to the a16z podcast. I’m Das, and in this episode, I talk SaaS go-to-market with David Ulevitch and our newest enterprise general partner Kristina Shen. The first half of the podcast looks at how remote work impacts the SaaS go-to-market and what the smartest founders are doing to survive the current crisis. The second half covers pricing approaches and strategy, including how to think about free versus paid trials and navigating the transition to larger accounts. But we start with why it’s easier to move upmarket than down… and the advantage that gives a SaaS startup against incumbents.
David : If you have a cohort of customers that are paying you $10,000 a year for your product, you’re going to find a customer that self-selects and is willing to pay $100,000 a year. Once you get one of those, your organization will figure out how you sell to, how you satisfy and support, customers at that price point and that size. But it’s really hard for a company that sells up market to move down market, because they’ve already baked in all that expensive, heavy lifting sales motion. And so as you go down market with a lower price point, usually, you can’t actually support it.
Das : Does that mean that it’s easier for a company to do this go-to-market if they’re a new startup as opposed to if they’re a pre-existing SaaS?
Kristina : It’s culturally very, very hard to give a product away for free that you’re already charging for. It feels like you’re eating away at your own potential revenue when you do it. So most people who try it end up pulling back very quickly.
David : This is actually one of the key reasons why the bottoms up SaaS motion is just so competitive, and compelling, and so destructive against the traditional sales-driven test motion. If you have that great product and people are choosing to use it, it’s very hard for somebody with a sales-driven motion, and all the cost that’s loaded into that, to be able to compete against it. There are so many markets where initially, we would look at companies and say, “Oh, well, this couldn’t possibly be bottoms up. It has to be sold to the CIO. It has to be sold to the CSO or the CFO.” But in almost every case we’ve been wrong, and there has been a bottoms up motion. The canonical example is Slack. It’s crazy that Slack is a bottoms up company, because you’re talking about corporate messaging, and how could you ever have a messaging solution that only a few people might be using, that only a team might be using? But now it’s just, “Oh, yeah, some people started using it, and then more people started using it, and then everyone had Slack.”
Kristina : I think another classic example is Dropbox versus Box. Both started as bottoms up businesses, try before you buy. But Box quickly found, “Hey, I'd rather sell to IT.” And Dropbox said, “Hey, we've got a great freemium motion going.” And they catalyzed their business around referrals and giving away free storage and shared storage in a way that really helped drive their bottoms up business.
Das : It's a big leap to go from selling to smaller customers to larger customers. How have you seen SaaS companies know or get the timing right on that? Especially since it does seem like that's really related to scaling your sales force?
Kristina : Don't try to go from a 100-person company to a 20,000-person company. Start targeting early adopters, maybe they're late stage pre-IPO companies, then newly IPO'd companies. Starting in tech tends to be a little bit easier because they tend to be early adopters. Going vertical by vertical can be a great strategy as well. Targeting one customer who might be branded in that space, can help brand yourself in that category. And then all their competitors will also want your product if you do a good job. A lot of times people will dedicate a sales rep to each vertical, so that they become really, really knowledgeable in that space, and also build their own brand and reputation and know who are the right customers to target.
Das : So right now, you've got a lot more people working remote. Does this move to remote work mean that on-premise software is dying? And is it accelerating the move to software as a service?
'''
# a = text.split()
print('text length:', len(text))
# print(summarizer(text))
# use bart in pytorch
# summarizer = pipeline("summarization")
# summarizer("An apple a day, keeps the doctor away", min_length=5, max_length=20)

# use t5 in tf
summarizer = pipeline("summarization", model="knkarthick/MEETING_SUMMARY")
# summarizer(text, min_length=5, max_length=20)
# summarizer = pipeline("summarization")
summary = summarizer(text, max_length = 200, min_length = 150)
a = summary[0]['summary_text']
print(a)
# a = summary[0]['summary_text'].split()
# print(len(a))
