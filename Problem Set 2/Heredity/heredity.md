## Heredity AI: Genetic Trait Prediction

### Overview:
This project involves creating an AI that assesses the likelihood that a person will exhibit a specific genetic trait, based on their genetic makeup and the genetic traits of their parents. The genetic trait under consideration is related to hearing impairment caused by the mutated version of the GJB2 gene. The task is to build a Bayesian Network that will calculate the probability of an individual inheriting a particular genetic trait.

### Problem Description:
Each person in the dataset carries two versions of the GJB2 gene, and the presence of the mutated gene is linked to hearing impairment. The goal is to infer the probability distribution of genetic traits in individuals based on family history and observed traits. For each person, the AI will calculate the likelihood of possessing 0, 1, or 2 copies of the gene, as well as the likelihood of exhibiting the trait associated with the gene.

### Key Concepts:
- **Gene Inheritance**: Children inherit one copy of the GJB2 gene from each parent. If both parents have the mutated gene, the child will have a high probability of inheriting the trait. If a parent has one copy of the gene, there is a 50% chance that the child will inherit the mutated version.
- **Gene Mutation**: After inheritance, there is a probability that the gene might mutate, changing from the gene associated with hearing impairment to a normal gene and vice versa.
- **Trait Expression**: The likelihood that a person exhibits a trait (e.g., hearing impairment) depends on the number of mutated gene copies they have. This likelihood is represented by conditional probabilities.

### Functions to Implement:
1. **`joint_probability()`**:
   - This function calculates the joint probability of all genetic events and trait expressions based on family data.
   - **Inputs**: `people`, `one_gene`, `two_genes`, `have_trait`.
     - `people`: A dictionary representing the family members.
     - `one_gene`: A set of people with one copy of the gene.
     - `two_genes`: A set of people with two copies of the gene.
     - `have_trait`: A set of people exhibiting the trait.
   - The function uses conditional probabilities to compute the likelihood of each scenario (such as a person having 0, 1, or 2 copies of the gene and exhibiting the trait or not).
   
2. **`update()`**:
   - This function updates the probability distributions for each person in the family, incorporating the computed joint probability.
   - **Inputs**: `probabilities`, `one_gene`, `two_genes`, `have_trait`, `p`.
     - `probabilities`: A dictionary of calculated probabilities for each individual.
     - `p`: The computed joint probability.
   - The function will add the joint probability `p` to the respective "gene" and "trait" distributions for each person.

3. **`normalize()`**:
   - This function ensures that all probability distributions are normalized, meaning the sum of probabilities for each individual equals 1.
   - **Input**: `probabilities`.
     - `probabilities`: A dictionary of people, with each person’s "gene" and "trait" distributions.
   - It adjusts the probabilities to ensure they are proportional and sum to 1.

### Dataset Structure:
The dataset `family0.csv` contains the following columns:
- **name**: The name of the person.
- **mother**: The name of the person's mother (if applicable).
- **father**: The name of the person's father (if applicable).
- **trait**: A binary value (1 for exhibiting the trait, 0 for not exhibiting it, or None if unknown).

### Example Data:
```csv
name,mother,father,trait
Harry,Lily,James,
James,,,1
Lily,,,0

