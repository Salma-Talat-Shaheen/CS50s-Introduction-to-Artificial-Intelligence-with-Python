# PageRank Algorithm

## Deadline
**Due date:** Thursday, January 1, 2026 at 1:59 AM GMT+2

## Getting Help
- Ask questions via Ed!
- Ask questions via CS50’s communities!

## Background
Search engines rank pages based on their "importance," which is determined by how many other pages link to a given page. However, simply counting the number of incoming links isn't sufficient, as a page can artificially inflate its importance by creating many other pages linking to it.

## PageRank Overview
PageRank is an algorithm designed by Google's co-founders that considers the importance of the page linking to a given webpage. A webpage is considered more important if it is linked to by other important pages. This system is circular, and it turns out there are various methods for calculating PageRank.

### Random Surfer Model
The random surfer model imagines a person randomly surfing the web, following links from one page to another. If a page has many incoming links, it becomes more likely that the surfer will visit that page. The probability of visiting a page is proportional to its importance, which is determined by the links leading to it.

**Damping Factor:** In this model, the damping factor `d` (usually around 0.85) accounts for the probability that the surfer will follow a link on the current page, versus jumping randomly to any other page in the corpus.

### Iterative Algorithm
PageRank can also be calculated using an iterative method, where each page's rank is recalculated using the ranks of the pages that link to it. The formula is as follows:

\[
PR(p) = \frac{1 - d}{N} + d \sum_{i \in inlinks(p)} \frac{PR(i)}{NumLinks(i)}
\]

Where:
- \(PR(p)\) is the PageRank of page `p`,
- \(d\) is the damping factor,
- \(N\) is the total number of pages,
- `inlinks(p)` is the set of pages that link to `p`,
- `NumLinks(i)` is the number of links on page `i`.

## Problem Description
The problem is to implement the PageRank algorithm to rank a set of web pages based on their importance. There are two main methods for solving this problem:

### Sampling Method
Estimate the PageRank of each page by simulating random surfing over the corpus. The rank is determined by the number of times a page is visited during random sampling.

### Iterative Method
Calculate the PageRank of each page using an iterative approach based on the formula provided above.

## Input
You are given a corpus of web pages, represented as a dictionary where the keys are page names (such as "1.html", "2.html", etc.), and the values are sets of pages that link to each page. The corpus is crawled from a website and is given as an argument in the form of a directory.

## Output
The output should display the estimated PageRank values for each page in the corpus, calculated using both the sampling and iteration methods.

## Specifications
### Transition Model
This model calculates the probability distribution over the next page that a random surfer will visit, given the current page and the corpus of pages.

### Sampling Method
Simulate random surfing over the corpus, with a fixed number of samples (e.g., 10,000). Count the number of times each page is visited, and use these counts to estimate the PageRank values.

### Iterative Method
Use an iterative approach where each page’s rank is updated based on the ranks of the pages that link to it. Continue updating the ranks until they converge to within a small threshold (e.g., 0.001).

## Implementation Details
### Corpus Representation
The corpus is a dictionary where each key is a page name and each value is a set of pages that link to that page. If a page has no outgoing links, treat it as if it links to all other pages.

### Damping Factor
Use a damping factor `d` of 0.85, which is typical in PageRank calculations.

### Iterations
In the iterative method, the algorithm should continue updating the ranks until the changes between iterations are smaller than a threshold (e.g., 0.001).

### Sampling
The sampling method involves selecting a random page, following links according to the transition model, and counting how often each page is visited.

## Example
Given the following simple corpus of 4 pages:
- 1.html links to 2.html and 3.html,
- 2.html links to 1.html,
- 3.html links to 2.html and 4.html,
- 4.html has no outgoing links (it links to all pages).


## Requirements
- **Python Version:** Python 3.12 is recommended.
- **Input Format:** The corpus is given as a dictionary.
- **Output Format:** The program should output the PageRank of each page, sorted by page name.

### Notes
- The algorithm may take a few seconds to run depending on the size of the corpus and the number of samples.
- The output should list the estimated PageRank values for each page, both from the sampling and iterative methods.

## Key Concepts
- **PageRank:** The algorithm used to rank web pages based on the number and quality of incoming links.
- **Random Surfer:** A model of how a random user would navigate the web, contributing to the calculation of PageRank.
- **Damping Factor:** The probability that the surfer will continue to follow links rather than jump randomly to another page.
- **Convergence:** The process of updating the PageRank values iteratively until they stabilize.

## Conclusion
The PageRank algorithm is essential for ranking web pages based on their importance. The two methods for estimating PageRank (sampling and iteration) provide useful approaches to understanding how the algorithm works. By simulating random surfing or iterating based on link structures, we can rank pages in a way that reflects their importance within a network of web pages.


