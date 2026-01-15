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
    let result = slidingWindowDynamic(array: [2, 3, 1, 2, 4, 3], target: 7)
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

func slidingWindowDynamic(array: [Int], target: Int) -> Int {
    var sum = 0
    var leftIndex = 0
    var minLength = Int.max
    for rightIndex in 0..<array.count {
        sum += array[rightIndex]
        
        while sum >= target {
            let currentLength = rightIndex - leftIndex + 1
            minLength = min(minLength, currentLength)
            sum = sum - array[leftIndex]
            leftIndex += 1
        }
    }
    return minLength == Int.max ? 0 : minLength
}

kickStarter()
