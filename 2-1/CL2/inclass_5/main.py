import pandas as pd

def load_gap_data(limit=25):
    """
    Load and preprocess the GAP dataset.
    Args:
        limit (int): Number of test cases to process (default: 25)
    Returns:
        pandas.DataFrame: Preprocessed dataframe with the first n test cases
    """
    # Read the CSV file
    # Assuming the data structure matches what you provided
    df = pd.read_csv('test.csv')
    
    # Take the first n test cases
    df = df.head(limit)
    
    # Clean up column names if needed
    df.columns = df.columns.str.strip()
    
    # Basic validation
    required_columns = ['ID', 'Text', 'Pronoun', 'A', 'B', 'A-coref', 'B-coref']
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    
    # Convert boolean columns to proper boolean type
    df['A-coref'] = df['A-coref'].astype(bool)
    df['B-coref'] = df['B-coref'].astype(bool)
    
    return df

def analyze_gap_dataset():
    """
    Main function to run all analyses on the GAP dataset
    """
    # Load the data
    try:
        data = load_gap_data()
        
        # Run analyses
        # print("\n1. Extracting Candidates:")
        # print("-" * 50)
        candidates = task2_extract_candidates(data)
        antecedents = task3_analyze_correct_antecedents(data)
        print(f"{'ID':<8} Pronoun  Candidates{' '*51} Antecedent")
        print("-" * 100)
        for i in range(25):
            c = candidates[i]
            a = antecedents[i]
            spc = '\t' * (7 - len(str(c['Candidates'])[:-6])//8)
            print(f"{c['ID']}:{' ' * (7 - len(c['ID']))} {c['Pronoun']}\t  {c['Candidates']}{spc}{a['Antecedent']}")
            # print(f"Example {i}:")
            # print(f"ID: {c['ID']}")
            # print(f"Pronoun: {c['Pronoun']}")
            # print(f"Candidates: {c['Candidates']}\n")
        recency_results = task4_analyze_recency(data)
        print(f"Total cases: {recency_results['total_cases']}")
        print(f"Correct based on recency: {recency_results['recent_correct']}")
        print(f"Accuracy: {recency_results['accuracy']:.2%}")
            
        # print("\n2. Analyzing Correct Antecedents:")
        # print("-" * 50)
        # for i, a in enumerate(antecedents[:3], 1):
        #     print(f"Example {i}:")
        #     print(f"ID: {a['ID']}")
        #     print(f"Pronoun: {a['Pronoun']}")
        #     print(f"Correct Antecedent: {a['Antecedent']}")
        #     print(f"Properties: {a['Properties']}\n")
            
        # print("\n3. Analyzing Recency:")
        # print("-" * 50)
        # print(f"Total cases: {recency_results['total_cases']}")
        # print(f"Correct based on recency: {recency_results['recent_correct']}")
        # print(f"Accuracy: {recency_results['accuracy']:.2%}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Updated analysis functions to accept dataframe parameter
def task2_extract_candidates(df):
    """Extract all candidate noun phrases (A and B) for each pronoun."""
    candidates = []
    for _, row in df.iterrows():
        candidates.append({
            'ID': row['ID'],
            'Pronoun': row['Pronoun'],
            'Candidates': [row['A'], row['B']]
        })
    return candidates

def task3_analyze_correct_antecedents(df):
    """Identify correct antecedents and their properties."""
    correct_antecedents = []
    for _, row in df.iterrows():
        # Get correct antecedent
        correct_ant = row['A'] if row['A-coref'] else (row['B'] if row['B-coref'] else None)
        
        properties = {
            'ID': row['ID'],
            'Pronoun': row['Pronoun'],
            'Antecedent': correct_ant or '-',
            # 'Properties': {
            #     'Gender': 'Male' if row['Pronoun'].lower() in ['he', 'his', 'him'] else 'Female',
            #     'Case': 'Subject' if row['Pronoun'].lower() in ['he', 'she'] else 'Object/Possessive',
            #     'Distance': 'Near' if row['Text'].find(correct_ant) < row['Text'].find(row['Pronoun']) else 'Far'
            # }
        }
        correct_antecedents.append(properties)
    return correct_antecedents

def task4_analyze_recency(df):
    """Analyze how often the most recent candidate is correct."""
    total = len(df)
    recent_correct = sum([1 if row['A-coref'] else 0 for _, row in df.iterrows()])
    print(f"incorrect: {', '.join([row['ID'][5:] for _, row in df.iterrows() if not row['A-coref']])}")
    
    return {
        'total_cases': total,
        'recent_correct': recent_correct,
        'accuracy': recent_correct / total
    }

if __name__ == "__main__":
    analyze_gap_dataset()