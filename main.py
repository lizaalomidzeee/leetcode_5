def moveZeroes(nums):
    last_non_zero_index = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero_index] = nums[i]
            last_non_zero_index += 1
    
    for i in range(last_non_zero_index, len(nums)):
        nums[i] = 0
    
    return nums

# ვუვლი მთლიან მასივს და ყველა ელემენტს, რომელიც არ არის ნოლი ვაყენებთ წინ. როცა ყველა არანულოვანი ელემენტი წინ გადავა, მივალ იმ ადგილამდე, სადაც 0-ები არიან და მათ ჩავწერ უკან.