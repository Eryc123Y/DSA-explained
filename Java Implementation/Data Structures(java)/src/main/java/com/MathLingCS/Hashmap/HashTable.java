package com.MathLingCS.Hashmap;

import com.MathLingCS.Array.DynamicArray;
import org.jetbrains.annotations.NotNull;

import java.util.Objects;
import java.util.Optional;

public abstract class HashTable<V> {

    protected static class Entry<V> implements Comparable<Entry<V>> {
        protected String key;
        protected V value;
        protected boolean deleted;

        protected Entry(String key, V value) {
            this.key = key;
            this.value = value;
            this.deleted = false;
        }

        @Override
        public int compareTo(@NotNull HashTable.Entry<V> o) {
            return this.key.compareTo(o.key);
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            Entry<?> entry = (Entry<?>) obj;
            return Objects.equals(key, entry.key);
        }

        @Override
        public int hashCode() {
            return Objects.hash(key);
        }
    }

    protected int size;
    protected int capacity;
    protected double loadFactor;
    protected DynamicArray<Entry<V>> table;
    protected final int[] TableSizes = {11, 23, 47, 97, 197, 397, 797, 1597, 3203,
            6421, 12853, 25717, 51437, 102877, 205759, 411527, 823117,
            1646237, 3292489, 6584983, 13169977, 26339969, 52679969,
            105359939, 210719881, 421439783, 842879579, 1685759167};
    protected final int HASH_Base = 31;
    int sizeIndex = 0;

    public HashTable() {
        capacity = TableSizes[sizeIndex];
        loadFactor = 0;
        table = new DynamicArray<>(capacity);
        for (int i = 0; i < capacity; i++) {
            table.add(null);
        }
    }

    // 抽象方法
    public abstract V get(String key);
    public abstract void put(String key, V value);
    public abstract void remove(String key);
    public abstract boolean containsKey(String key);

    // 辅助方法
    protected abstract int hash(String key);
    protected abstract int probe(String key, int index);
    protected abstract void rehash();

    // 通用方法
    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public double getCurrentLoadFactor() {
        return (double) size / capacity;
    }

    public Optional<V> getOptional(String key) {
        return Optional.ofNullable(get(key));
    }

    public V getOrDefault(String key, V defaultValue) {
        V value = get(key);
        return value != null ? value : defaultValue;
    }
}
