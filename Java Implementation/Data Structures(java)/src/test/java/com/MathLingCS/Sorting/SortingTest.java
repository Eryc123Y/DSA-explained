package com.MathLingCS.Sorting;

import com.google.common.truth.Truth;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import com.MathLingCS.Sorting.BubbleSort;
import com.MathLingCS.Sorting.InsertionSort;
import com.MathLingCS.Sorting.SelectionSort;
import com.MathLingCS.Sorting.CocktailSort;

import java.util.ArrayList;
import java.util.Arrays;

@SuppressWarnings("unused")
public class SortingTest {
    private ArrayList<Integer> list;
    private ArrayList<Integer> sortedList;
    private final Sort sort1 = new BubbleSort();
    private final Sort sort2 = new InsertionSort();
    private final Sort sort3 = new SelectionSort();
    private final Sort sort4 = new CocktailSort();


    @BeforeEach
    public void setUp() {
        list = new ArrayList<>(Arrays.asList(5, 3, 8, 6, 2, 7, 1, 4));
        sortedList = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8));
    }

    @Test
    public void testBubbleSort() {
        var array = list.toArray(new Integer[0]);
        var sortedArray = sort1.sort(array);
        Truth.assertThat(Arrays.asList(sortedArray)).isEqualTo(sortedList);
    }

    @Test
    public void testInsertionSort() {
        var array = list.toArray(new Integer[0]);
        var sortedArray = sort2.sort(array);
        Truth.assertThat(Arrays.asList(sortedArray)).isEqualTo(sortedList);
    }

    @Test
    public void testSelectionSort() {
        var array = list.toArray(new Integer[0]);
        var sortedArray = sort3.sort(array);
        Truth.assertThat(Arrays.asList(sortedArray)).isEqualTo(sortedList);
    }

    @Test
    public void testCocktailSort() {
        var array = list.toArray(new Integer[0]);
        var sortedArray = sort4.sort(array);
        Truth.assertThat(Arrays.asList(sortedArray)).isEqualTo(sortedList);
    }
}
