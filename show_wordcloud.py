# Install required libraries
# pip install wordcloud matplotlib numpy

import matplotlib.pyplot as plt
from wordcloud import WordCloud

sample_text = "GitHub Actions for CI/CD \
GitHub Packages for container hosting \
Protected branches on all repos \
Access to Code spaces\
Multiple reviewers in pull requests \
Required status checks \
Code owners \
Reviewers \
Pages for static website hosting \
Web-based support"

# Create a WordCloud object
wordcloud_str2 = WordCloud(width=800, height=400, background_color='white').generate(sample_text)

# Display the generated word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_str2, interpolation='bilinear')
plt.axis('off')
plt.show()