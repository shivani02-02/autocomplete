'''
Created on Oct 31, 2019

@author: shivani.chauhan
'''
import csv
import operator

class Logic:
    word_list = []
    word_occ_dict = {}
    def read_tsv_file(self):
        with open(r"C:\Users\shivani.chauhan\Downloads\word_search.tsv") as file:
            for line in file:
                word, occ = line.split('\t')
                self.word_occ_dict[word] = occ
                self.word_list.append(word)
            
    
    def search_word(self, letters):
        results = []
        for word in self.word_list:
            if letters in word:
                results.append(word)
        return results
    
    
    def sorting(self, results, incomp):
        result_distances = [(result, result.find(incomp), self.word_occ_dict[result], len(result)) for result in results]
        result_distances.sort(key=lambda elem: (elem[3],elem[1]))
        searchResults = [(result_distance[0],result_distance[2]) for result_distance in result_distances][:25]
        return(searchResults)

# sorting(search_word('eta'), 'eta')