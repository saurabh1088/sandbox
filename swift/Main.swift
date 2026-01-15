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
    let result = newArrayByMovingAverage(array: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], window: 2)
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

func newArrayByMovingAverage(array: [Int], window: Int) -> [Double] {
    var sum = 0
    var finalArray = [Double]()
    for index in 0..<array.count {
        sum += array[index]
        
        if index >= window {
            sum = sum - array[index - window]
        }
        
        let base = index + 1 < window ? Double(index + 1) : Double(window)
        let average = Double(sum) / base
        finalArray.append(average)
    }
    return finalArray
}

kickStarter()
