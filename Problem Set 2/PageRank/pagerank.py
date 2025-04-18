import os
import random
import re
import sys
import copy

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus: dict, page: str, damping_factor: float) -> dict:
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.

    Args:
      corpus: dictionary mapping a page name to a set of all pages linked to by that page.
      page: string representing which page the random surfer is currently on.
      damping_factor: float representing the damping factor to be used when generating the probabilities.

    Returns:
      A probability distribution over which page to visit next as a
      dictionary.
    """
    no_outgoing_links = len(corpus[page]) < 1

    if no_outgoing_links:
        return calculate_distributions_at_random_from_all_possible_pages(corpus)
    else:
        return calculate_probability_distributions(corpus, page, damping_factor)


def calculate_distributions_at_random_from_all_possible_pages(corpus: dict) -> dict:
    """
    Returns probability distributions by selecting randomly from all possible pages 
    within the given corpus.

    Specification:
      If page has no outgoing links, then transition_model should return a probability 
      distribution that chooses randomly among all pages with equal probability. 
      (In other words, if a page has no links, we can pretend it has links to all 
      pages in the corpus, including itself.
    """
    probability_distribution = {}
    corpus_length = len(corpus.keys())

    for page_name in corpus.keys():
        probability_distribution[page_name] = 1 / corpus_length

    return probability_distribution
        
        
def calculate_probability_distributions(corpus: dict, page:str, damping_factor: float) -> dict:
    """
    Returns probability distribution over which page to visit next, 
    given a current page.

    Specification:
    The return value of the function should be a Python dictionary with one key for each page in the corpus. 
    Each key should be mapped to a value representing the probability that a random surfer would choose that
    page next. The values in this returned probability distribution should sum to 1. 

    With probability damping_factor, the random surfer should randomly choose one of the links from page with
    equal probability.

    With probability 1 - damping_factor, the random surfer should randomly choose one of all pages in the corpus
    with equal probability.
    """
    probability_distribution = {}
    corpus_length = len(corpus.keys())
    page_length = len(corpus[page])
    random_factor = (1 - damping_factor) / corpus_length
    
    for page_name in corpus.keys():
        if page_name not in corpus[page]: 
            probability_distribution[page_name] = random_factor
        else:
            probability_distribution[page_name] = random_factor + (damping_factor / page_length) 

    return probability_distribution


def sample_pagerank(corpus: dict, damping_factor: float, n: int) -> dict:
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Args:
      corpus: dictionary mapping a page name to a set of all pages linked to by that page.
      damping_factor: float representing the damping factor to be used when generating the probabilities.
      n: integer representing the number of samples that should be generated to estimate PageRank values.

    Returns:
      PageRank values as dictionary where keys are page names, and values are
      their estimated PageRank value (a value between 0 and 1). All
      PageRank values should sum to 1.
    """
    page_rank = {}.fromkeys(corpus.copy().keys(), 0) # initialise page ranks as 0
    sample = None

    for _ in range(n):
        if sample:
            probability_distribution = transition_model(corpus, sample, damping_factor)
            page_names = list(probability_distribution.keys())
            weights = [probability_distribution[i] for i in probability_distribution]
            sample = random.choices(page_names, weights, k=1)[0]
        else:
            sample = random.choice(list(corpus.keys()))

        page_rank[sample] += 1


    for page_name in page_rank:
        page_rank[page_name] /= n

    print(f"Sum: {sum(page_rank.values())}")


    return page_rank


def iterate_pagerank(corpus: dict, damping_factor: float) -> dict:
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Args:
      corpus: dictionary mapping a page name to a set of all pages linked to by that page.
      damping_factor: float representing the damping factor to be used when generating the probabilities.

    Returns:
      PageRank values as dictionary where keys are page names, and values are
      their estimated PageRank value (a value between 0 and 1). All
      PageRank values should sum to 1.
    """
    corpus_length = len(corpus)
    old_page_rank = {}
    new_page_rank = {}

    for page_name in corpus: 
        # initialise equal page ranks as 1 / pages in corpus
        old_page_rank[page_name] = 1 / corpus_length 

    while True:
        for i in corpus:
            link_weight = 0
            for j in corpus:
                page_has_no_links = len(corpus[j]) == 0
                page_links_to_current_page = i in corpus[j]

                if page_links_to_current_page:
                    link_weight += (old_page_rank[j] / len(corpus[j]))

                if page_has_no_links:
                    link_weight += (old_page_rank[j]) / corpus_length

            link_weight *= damping_factor
            link_weight += (1 - damping_factor) / corpus_length

            new_page_rank[i] = link_weight

        reached_convergence = max([abs(new_page_rank[x] - old_page_rank[x]) for x in old_page_rank]) < 0.001
        
        if reached_convergence :
            break
        else:
            old_page_rank = new_page_rank.copy()

    print(f"Sum: {sum(old_page_rank.values())}")


    return old_page_rank


if __name__ == "__main__":
    main()
