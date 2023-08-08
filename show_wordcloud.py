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
wordcloud_str = WordCloud(width=800, height=400, background_color='white').generate(sample_text)

# Display the generated word cloud
# plt.switch_backend('TkAgg')
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_str, interpolation='bilinear')
plt.axis('off')
# Show the wordcloud as an image in Matlab simulator
# plt.show()

# Save the wordcloud as a png image file
plt.savefig('./wordcloud.png')
