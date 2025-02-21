# Hackathon - Brand Name Similarity for Criteo

## Overview 

This hackathon project aims to unify and standardize brand names for Criteo by computing similarity between brands. By combining multiple similarity metrics into a weighted approach, our solution can automatically group brands that share common online footprints. A key component of our project involves using API calls to perform web scraping—extracting the first five Google search links for each brand—to help determine if different brand name variations actually refer to the same entity.

## Motivation

In retail media for example, accurate brand representation is essential for successful advertising. Criteo’s initiative to unify brand names plays a critical role in optimizing their retail media offerings. Consistency in brand naming directly impacts:

- Enhanced Retail Media Targeting:
Accurate brand representation ensures that advertisements are correctly associated with trusted and recognized brands, boosting ad relevancy, click-through rates, and conversions.
- Consistency Across Retail Channels:
Standardized brand names improve the consumer journey by reducing confusion across multiple e-commerce platforms, ultimately fostering trust and loyalty.
- Improved Data Analytics:
Unified brand naming facilitates data aggregation and deeper analysis, enabling advertisers to make more informed decisions and optimize marketing spend.
- Strategic Advantage:
A consolidated view of brand data provides Criteo with a competitive edge in retail media, attracting advertisers who value high accuracy and consistency.

By solving this problem, Criteo not only enhances its service offering to existing clients but also significantly boosts the ROI of their ad campaigns by ensuring that each ad reaches its intended audience more effectively. This precise targeting reduces ad waste and maximizes the impact of each marketing dollar spent. Furthermore, Criteo positions itself as a leader in retail media solutions capable of handling complex data challenges. This capability strengthens its market position and opens up opportunities for onboarding new brands facing similar challenges, expanding its client base and potentially increasing overall company revenue 

## Technical Approach

1. **Data Cleaning and Preprocessing**

**Translation & Cleaning**:
Our pipeline begins by cleaning the raw brand data. This involves translating text from Korean to English and removing special characters and extraneous text. 
The cleaned data is then saved as a CSV file (<font color="blue">fully_cleaned.csv</font>), which serves as the foundation for all subsequent analyses.

2. **Similarity Computation**

Initial Similarity Analysis:
The cleaned CSV is processed in the <font color="blue">similarity.ipynb</font> notebook, where we compute similarity between brand names using various metrics—such as fuzzy matching and Jaccard similarity. The final similarity values are then encapsulated in the <font color="blue">similarities.py</font> module, which offers easy-to-use functions for comparing both brand names and descriptions.
Weighted Similarity Computation:
In the weighted_score.ipynb notebook, we apply a weighted similarity approach. This method aggregates similar sub-brands—such as grouping “Versace Jeans” and “Versace Kids” under the umbrella of “Versace”—by leveraging high similarity scores. The output is a DataFrame where brands with high internal similarity are clustered together.

3. **API Integration and Data Enrichment**

**Web Scraping & External Data:**
After the initial similarity computations, <font color="blue">Hackathon_Brand_added_details.ipynb</font> calls external APIs to fetch additional data, including product descriptions, images, and URLs for each brand. This enrichment phase adds a new dimension to our dataset.
Advanced Brand Unification:
With the added context from the API (e.g., product details and online content), our process goes a step further: even if brand names differ significantly in text (for example, “HP” versus “Hewlett Packard”), the enriched data helps us identify and merge them as the same entity.

4. **Future possible imporvments**
   
 **Composite Similarity Metric:** In future iterations, we could enhance our model by assigning specific weights to the comparisons of various attributes—such as links, images, descriptions, and brand names. By integrating these weighted comparisons, we will compute a final composite similarity metric. Once the composite metric is calculated, brands with similarity scores exceeding a predefined threshold will be grouped together. This will enable even more accurate brand unification, ensuring that different representations of the same brand (like abbreviations and full names) are correctly merged.


## Business Impact for Criteo 

1. Enhanced Ad Targeting and Efficiency:

- Direct Impact: By standardizing brand names across all platforms, Criteo can significantly improve the accuracy of its ad targeting algorithms. This leads to higher engagement rates as ads are more relevant to the users’ interests and search histories.
- Operational Efficiency: More accurate targeting reduces wasted ad spend and increases the effectiveness of advertising budgets. For Criteo, this means better performance metrics to present to clients, enhancing client satisfaction and retention.

2. Strengthened Analytics and Data Insights:

- Improved Data Quality: Unified brand names consolidate data silos, leading to cleaner datasets that are easier to analyze. This improvement in data quality enhances the reliability of performance analytics and KPIs.
- Strategic Decision-Making: With more reliable data, Criteo can offer deeper insights into consumer behavior and brand performance. This enables more informed decision-making for both Criteo and its clients, facilitating strategies that are data-driven and result-oriented.

3. Increased Revenue Opportunities:

- New Market Penetration: Clear and consistent brand data allows Criteo to more effectively manage campaigns for brands looking to enter new markets or expand in existing ones. This capability can be a major selling point when attracting new clients.
- Upselling Advanced Services: With foundational data issues resolved, Criteo can focus on upselling more sophisticated and higher-margin services like predictive analytics and personalized ad solutions.

4. Enhanced Client Relationships and Trust:

- Brand Trust: Consistency in how brands are presented in advertisements helps maintain the integrity of the brand, which is crucial for client trust and satisfaction.
- Long-term Partnerships: By delivering consistently successful outcomes through improved targeting and analytics, Criteo can foster long-term relationships with its clients. This reliability can make Criteo a preferred partner for digital advertising services.

5. Compliance and Reputation Management:

- Regulatory Compliance: Unified brand naming helps ensure compliance with global advertising standards and regulations, reducing the risk of legal issues related to misrepresentation or incorrect branding.
- Enhanced Corporate Image: Successfully managing brand data also improves Criteo's reputation in the market as a data-savvy and client-centric advertising technology provider.

6. Scalability and Technological Leadership:

- Foundation for Future Innovation: With a unified approach to brand names, Criteo can more easily implement emerging technologies such as AI and machine learning for even more advanced data handling and ad targeting techniques.
- Leadership in Ad Tech: By addressing and solving complex data consistency issues, Criteo reinforces its position as a leader in the advertising technology sector, capable of handling the sophisticated needs of global brands.


## Team

**AL NABBOUT Christina**

**BOUSQUET Capucine**

**FERRACINI Clara Maria**

**SHARMA Manvi**