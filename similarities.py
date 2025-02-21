from nltk.corpus import words
import pandas as pd


# Assuming the words corpus is already downloaded:
# nltk.download('words')

english_vocab = set(w.lower() for w in words.words())

# add common words in brand names words to the english vocab so they're considered as common english words
english_vocab.update(["johnson", "co", "dr", "wd"])

def weighted_score(s1, s2, english_vocab, brand_weight=2.0, common_weight=1.0):
    """
    Compute a Weighted Jaccard similarity between two pre-cleaned, lowercased strings s1 and s2.
    - Tokens not in english_vocab are assigned a higher weight (brand_weight).
    - Tokens in english_vocab have a lower weight (common_weight).
    Returns an integer score between 0 and 100, similar to fuzz.ratio.
    
    Parameters:
      s1, s2: Input strings (assumed already lower case, stripped, and cleaned).
      english_vocab: A set of common English words.
      brand_weight: Weight for non-English words (assumed to be brand-like).
      common_weight: Weight for common English words.
      
    Returns:
      An integer similarity score between 0 and 100.
    """
    # Tokenize strings into sets
    tokens1 = set(s1.split())
    tokens2 = set(s2.split())
    
    # Compute union and intersection
    union_tokens = tokens1.union(tokens2)
    intersection_tokens = tokens1.intersection(tokens2)

    # Handle edge case: if no tokens exist
    if not union_tokens:
        return 0
    
    # Function to determine token weight
    def token_weight(token):
        return brand_weight if token not in english_vocab else common_weight
    
    # Compute weighted intersection and weighted union
    weighted_intersection = sum(token_weight(t) for t in intersection_tokens)
    weighted_union = sum(token_weight(t) for t in union_tokens)

    # Compute weighted similarity
    weighted_score = weighted_intersection / weighted_union

    # Convert to percentage scale (0-100)
    return int(weighted_score * 100)

def filter_brands(df, column_name, threshold=70, score_func=weighted_score, english_vocab=english_vocab, brand_weight=2.0, common_weight=1.0):
    """
    Filter pairs of brand names whose similarity score (computed using score_func)
    exceeds the given threshold.
    
    Assumes the brand names in the DataFrame are already in lower case, stripped,
    and with special characters removed.
    
    Parameters:
      df: Pandas DataFrame containing the brand data.
      column_name: Name of the column with brand names.
      threshold: Similarity threshold (default 70, matching a percentage score).
      score_func: Function to compute similarity between two strings.
      english_vocab: Set of common English words.
      brand_weight: Weight for non-English words.
      common_weight: Weight for common English words.
      
    Returns:
      A list of tuples (brand1, brand2, score) for pairs with score > threshold.
    """
    filtered_brands = []
    brands = [str(brand).strip() for brand in df[column_name].tolist() if pd.notnull(brand)]
    seen_pairs = set()
    
    for i, brand1 in enumerate(brands):
        for j, brand2 in enumerate(brands):
            if i != j and brand1 != brand2:
                pair = tuple(sorted((brand1, brand2)))
                if pair not in seen_pairs:
                    seen_pairs.add(pair)
                    score = score_func(brand1, brand2, english_vocab, brand_weight=brand_weight, common_weight=common_weight)
                    if score > threshold:
                        filtered_brands.append((brand1, brand2, score))
    
    return filtered_brands

def filter_brands_text(df, desc_col, brand_name, threshold=70, 
                       score_func=weighted_score, english_vocab=english_vocab, 
                       brand_weight=2.0, common_weight=1.0):
    """
    Filter pairs of brand descriptions based on their similarity score computed using score_func.
    For each pair that exceeds the threshold, return a tuple:
      (description1, description2, brand_name1, brand_name2, score)
    
    Parameters:
      df: Pandas DataFrame containing the data.
      desc_col: Column name for brand descriptions.
      name_col: Column name for brand names.
      threshold: Similarity threshold (default 70).
      score_func: Function to compute similarity between two strings.
      english_vocab: Set of common English words.
      brand_weight: Weight for tokens not in english_vocab.
      common_weight: Weight for tokens in english_vocab.
      
    Returns:
      A list of tuples (desc1, desc2, name1, name2, score) for pairs with score > threshold.
    """
    filtered = []
    # Remove rows with missing descriptions or brand names
    df_clean = df[df[desc_col].notnull() & df[brand_name].notnull()]
    
    # Create a list of tuples (description, brand_name) for each row
    brand_data = [(str(row[desc_col]).strip(), str(row[brand_name]).strip()) 
                  for _, row in df_clean.iterrows()]
    
    n = len(brand_data)
    # Compare each unique pair only once
    for i in range(n):
        desc1, name1 = brand_data[i]
        for j in range(i + 1, n):
            desc2, name2 = brand_data[j]
            score = score_func(desc1, desc2, english_vocab, 
                               brand_weight=brand_weight, common_weight=common_weight)
            if score > threshold:
                filtered.append((desc1, desc2, name1, name2, score))
    return filtered


