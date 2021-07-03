   m1_i = int(len(nums1) / 2)
    m2_i = int(len(nums2) / 2)
     median1 = 0
      median2 = 0

       if len(nums1) % 2 != 0:
            median1 = nums1[m1_i]
        elif len(nums1) % 2 == 0 and len(nums1) != 0:
            median1 = (nums1[m1_i] + nums1[m1_i - 1]) / 2

        if len(nums2) % 2 != 0:
            median2 = nums2[m2_i]
        elif len(nums2) % 2 == 0 and len(nums2) != 0:
            median2 = (nums2[m2_i] + nums2[m2_i - 1]) / 2

        if len(nums1) != 0 and len(nums2) != 0:
            print(median1)
            print(median2)
            return (median1 + median2) / 2
        elif len(nums1) == 0:
            return median2
        else:
            return median1
