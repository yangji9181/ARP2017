## Implementation of *ARP*, SDM 2019.

Please cite the following work if you find the code useful.

```
@inproceedings{yang2019cube2net,
	Author = {Yang, Carl and Chang, Kevin},
	Booktitle = {SDM},
	Title = {Relationship profiling over social networks: reverse smoothness from similarity to closeness},
	Year = {2019}
}
```
Contact: Carl Yang (yangji9181@gmail.com)

As discussed in our ARP paper, we conduct various experiments and case studies on the public DBLP dataset downloaded from http://dblp.uni-trier.de. Here we present some insightful results to show the merits of our algorithm in some novel interesting applications.

### Repository Description

We uploaded all results presented in the paper, as well as some interesting figures generated from the results, together with the data we used and the code we wrote, for your exploration. The files are in the corresponding folders. The codes are wrote in python 2 and direcly runnable through the terminal. 

Since we have included all intermediate results (and final ones), you can run any python files in the code folder directly except for preprocess.py, which requires the original dblp.xml file. To run it, please download the DBLP dataset from http://dblp.dagstuhl.de/xml/release/ and put the dblp.xml file in the data folder. Note that different versions of the dataset might lead to minor divergence in the results. The version we used is dblp-2016-01-01.

### Visualization of Researcher vs. Researcher Multi-Relationships
In the following three figures, the x and y axis are the same set of researchers.

<img src="https://raw.githubusercontent.com/yangji9181/ARP2017/master/figures/holistic/kddheat.png" width="800" />

In the figure above, collaborations in data mining (KDD) are marked as red.

<img src="https://raw.githubusercontent.com/yangji9181/ARP2017/master/figures/holistic/icmlheat.png" width="800" />

In the figure above, collaborations in machine learning (ICML) are mared as red.

<img src="https://raw.githubusercontent.com/yangji9181/ARP2017/master/figures/holistic/vldbheat.png" width="800" />

In the figure above, collaborations in database (VLDB) are mared as red.

As we can see, the collaboration matrix is naturally sparse. While the three relationships cluster on different locations (thus among different set of authors), some collaborations indeed bare multiple relationships (the same red dots appear in multiple figures). Also, it is interesting to see that in the KDD plot, the red dots scatter quite strictly in the top-left corner, which means that only data mining people collaborate in data mining a lot. However, in both the ICML plot and the VLDB plot, while most red dots scatter in the corresponding locations (the center-center and bottom-right), some obviously appear in the ICML-KDD and VLDB-KDD locations. It clearly indicates that many data mining people also collaborate in machine learning and database. It is true because data mining people need to know both machine learning and database, but not vise versa.

Moreover, in both the second and the third figures, there is almost no red dot in the VLDB-ICML squares, which means database people seldomly collaborate in machine learning conferences and vise versa. 

We also draw the same three figures but with the single edge modeling configuration (instead of holistic modeling). We put the figures in the figures/single folder. The insightful observations are much harder to make with the single edge modeling approach. The red dots are much sparser, especially in the cross-field locations. E.g., in the figure icmlheat.png generated in the figures/single folder, we can hardly observe the collaborations in machine learning between data mining researchers and machine learning researchers, as we can observe clearly in the figure icmlheat.png generated in figures/holistic folder.

### Visualization of Venue vs. Venue Correlations

<img src="https://raw.githubusercontent.com/yangji9181/ARP2017/master/figures/vxvheat.png" width="800" />

The analyzed venues from top to bottom and from left to right are KDD, ICML and VLDB. We compute the correlations among venues by counting the number of links that are predicted with two relationships. As can be seen from this plot, the correlation between data mining and machine learning is higher than that between data mining and database, and the latter is higher than the correlation between machine learning and database. While the results shown are intuitive, it is trivial but insightful to apply the same analysis to any venues that are not so intuitively differenciable, such as WWW, SIGMOD, WSDM, CIKM, KDD and so on, to see how these similarly-themed venues attract the same collaborations.

### More to Come

The visualizations of our experimental results are quite basic now. However, as can be seen from the current results, our ARP algorithm is able to capture the precise relationships among every pair of authors based on any venue. Therefore, it enables many more novel interesting applications such as retrieving impactful collaborations within specific fields, understanding relationships through multiple angles, interpreting correlations among different fields, and so on. We are actively working on more interpretable and insightful analysis as well as visualizations and will be putting in more stuff soon!

