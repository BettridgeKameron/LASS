import { describe, it, expect, vi } from 'vitest';
import SentAnalyze from '@/views/SentimentAnalysis.vue';
import { mount } from '@vue/test-utils';

describe('SentimentAnalysis.vue', () => {
  it('should call the analyzeSentiment method when the button is clicked', async () => {
    const wrapper = mount(SentAnalyze);

    // Find the button element
    const button = wrapper.find('button');

    // Mock the analyzeSentiment method (optional)
    const mockAnalyzeSentiment = vi.fn();
    wrapper.vm.analyzeSentiment = mockAnalyzeSentiment; // Replace with actual method if needed

    // Trigger the click event on the button
    await button.trigger('click');

    // Assert that the analyzeSentiment method was called
    expect(mockAnalyzeSentiment).toHaveBeenCalled();
  });
});