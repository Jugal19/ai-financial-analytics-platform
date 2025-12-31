<template>
    <div class="max-w-7x1 mx-auto space-y-6">
        <div class="lg:col-span-3 bg-gray-800 rounded-xl p-6 border border-gray-700">
            <!-- Metrics -->
            <MetricCard title="Total Income" value="$12,400" />
            <MetricCard title="Total Expenses" value="$8,950" />
            <MetricCard title="Savings" value="$3,450" />

            <!-- Charts placeholder -->
            <div class="lg:col-span-2 bg-gray-900 rounded-xl p-6 border border-gray-800">
            <h3 class="text-lg font-semibold mb-4">Spending Trends</h3>
            <div class="h-48 flex items-center justify-center text-gray-500">
                Charts Placeholder
            </div>
            </div>
            <!-- AI Assistant -->
            <AIAssistant />
        </div>
    </div>
</template>

<script setup>
    import MetricCard from '../components/MetricCard.vue'
    import AIAssistant from '../components/AIAssistant.vue'
</script>