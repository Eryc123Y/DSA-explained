package com.MathLingCS.Hashmap;

import com.MathLingCS.Array.DynamicArray;

public class LinearProbTable<V> extends HashTable<V> {

    public LinearProbTable() {
        super();
    }

    @Override
    public V get(String key) {
        int index = hash(key);
        for (int i = 0; i < capacity; i++) {
            int newIndex = (index + i) % capacity;
            Entry<V> entry = table.get(newIndex);
            if (entry == null) {
                return null;
            } else if (!entry.deleted && entry.key.equals(key)) {
                return entry.value;
            }
        }
        return null;
    }

    @Override
    public void put(String key, V value) {
        if (getCurrentLoadFactor() > 0.75) {
            rehash();
        }
        int index = hash(key);
        for (int i = 0; i < capacity; i++) {
            int newIndex = (index + i) % capacity;
            Entry<V> entry = table.get(newIndex);
            if (entry == null || entry.deleted) {
                table.set(newIndex, new Entry<>(key, value));
                size++;
                break;
            } else if (entry.key.equals(key)) {
                entry.value = value;
                break;
            }
        }
        loadFactor = (double) size / capacity;
    }

    @Override
    public void remove(String key) {
        int index = hash(key);
        for (int i = 0; i < capacity; i++) {
            int newIndex = (index + i) % capacity;
            Entry<V> entry = table.get(newIndex);
            if (entry == null) {
                return; // key not found
            } else if (!entry.deleted && entry.key.equals(key)) {
                entry.deleted = true;
                size--;
                loadFactor = (double) size / capacity;
                return;
            }
        }
    }

    @Override
    public boolean containsKey(String key) {
        int index = hash(key);
        for (int i = 0; i < capacity; i++) {
            int newIndex = (index + i) % capacity;
            Entry<V> entry = table.get(newIndex);
            if (entry == null) {
                return false;
            } else if (!entry.deleted && entry.key.equals(key)) {
                return true;
            }
        }
        return false;
    }

    @Override
    protected int hash(String key) {
        int res = 0;
        for (int i = 0; i < key.length(); i++) {
            res = (res * HASH_Base + key.charAt(i)) % capacity;
        }
        return res;
    }

    @Override
    protected int probe(String key, int index) {
        for (int i = 0; i < capacity; i++) {
            int newIndex = (index + i) % capacity;
            Entry<V> entry = table.get(newIndex);
            if (entry == null || entry.deleted || entry.key.equals(key)) {
                return newIndex;
            }
        }
        return -1; // table is full
    }

    @Override
    protected void rehash() {
        DynamicArray<Entry<V>> oldTable = table;
        capacity = TableSizes[++sizeIndex];
        table = new DynamicArray<>(capacity);
        for (int i = 0; i < capacity; i++) {
            table.add(null);
        }
        size = 0;
        for (int i = 0; i < oldTable.size(); i++) {
            Entry<V> entry = oldTable.get(i);
            if (entry != null && !entry.deleted) {
                put(entry.key, entry.value);
            }
        }
    }
}
