import { describe, it, expect, vi } from 'vitest'
import SentAnalyze from '@/views/SentimentAnalysis.vue'
import { mount, shallowMount } from '@vue/test-utils'

describe('SentimentAnalysis.vue', () => {
  it('should initially display an empty text area', () => {
    const wrapper = shallowMount(SentAnalyze)
    const textarea = wrapper.find('textarea')
    expect(textarea.element.value).toBe('')
  })

  it('should call the analyzeSentiment method when the button is clicked', async () => {
    const wrapper = mount(SentAnalyze)

    const button = wrapper.find('button')

    const mockAnalyzeSentiment = vi.fn()
    wrapper.vm.analyzeSentiment = mockAnalyzeSentiment

    await button.trigger('click')

    expect(mockAnalyzeSentiment).toHaveBeenCalled()
  })

  it('textToAnalyze updates on user input', async () => {
    const wrapper = shallowMount(SentAnalyze)
    const input = wrapper.find('textarea')
    await input.setValue('This is a test sentence.')
    expect(wrapper.vm.textToAnalyze).toBe('This is a test sentence.')
  })

  it('analyzeSentiment clears error message before API call', async () => {
    const wrapper = shallowMount(SentAnalyze, {
      data() {
        return {
          errorMessage: 'Previous error message'
        }
      }
    })

    wrapper.vm.analyzeSentiment()
    await new Promise((resolve) => setTimeout(resolve, 0))
    expect(wrapper.vm.errorMessage).toBe('')
  })
})
