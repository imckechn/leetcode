class Solution:
    def merge(nums1, m, nums2, n) -> None:
        if n == 0:
            return
        
        if m == 0 and len(nums1) != 0:
            nums1 = []
        
        for i in range(m):
            nums1.pop()

        i = 0
        while len(nums1) > i:
            if nums1[i] > nums2[0]:
                nums1.insert(i, nums2[0])
                nums2.pop(0)
            i = i + 1

        nums1 = nums1 + nums2
        
        print(nums1)

def addIn(array, index, element):
    save1 = array[index]
    array[index] = element

    for i in range(index + 1, len(array)):
        save2 = array[i]
        array[i] = save1
        save1 = save2

Solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)

