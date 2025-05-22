function twoSum(nums: number[], target: number): number[] {
    const res: number[] = []
    for (let i: number = 0; i < nums.length; i = i + 1  ){
        for (let j: number = i+1; j < nums.length; j = j + 1){
            if (nums[j] + nums[i] == target) {
                res.push(i)
                res.push(j)
            }
        }
    }
    return res 
}

const nums: number[] = [1, 2, 3, 4];
const target: number = 6;

console.log(twoSum(nums, target))