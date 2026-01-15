//
//  Main.swift
//  
//
//  Created by Saurabh Verma on 15/01/26.
//

import Foundation

func kickStarter() {
    print("Hello, Sandbox!")
    print("Here we start!")
    let result = slidingWindowFixedType(array: [1, 2, 4, 5, 2, 6, 7, 9, 1, 2, 4, 5, 6, 7, 4], windowSize: 3)
    print(result)
}

func slidingWindowFixedType(array: [Int], windowSize: Int) -> Int {
    guard windowSize > 0, !array.isEmpty else {
        return 0
    }
    var finalSum = 0
    var currentSum = 0
    var leftIndex = 0
    
    for index in 0..<windowSize {
        currentSum += array[index]
    }
    
    finalSum = currentSum
    
    for index in windowSize..<array.count {
        currentSum = currentSum + array[index]
        currentSum = currentSum - array[index - windowSize]
        leftIndex += 1
        
        if currentSum > finalSum {
            finalSum = currentSum
        }
    }
    
    return finalSum
}

kickStarter()
