import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'
import { mount, VueWrapper } from '@vue/test-utils'
import StringInput from '../StringInput.vue'
import axios from 'axios'

vi.mock('axios', async () => {
  const actualAxios = await vi.importActual<any>('axios')
  return {
    ...actualAxios,
    default: {
      post: vi.fn()
    }
  }
})

describe('StringInput.vue', () => {
  let wrapper: VueWrapper<any>

  beforeEach(() => {
    wrapper = mount(StringInput)
  })

  afterEach(() => {
    vi.resetAllMocks()
  })

  it('should display reversed string when API call is successful', async () => {
    vi.mocked(axios.post).mockResolvedValueOnce({ data: { reversed_string: 'gnirtS' } })

    wrapper.vm.userInput = 'String'
    await wrapper.vm.sendString()

    await wrapper.vm.$nextTick()
    expect(wrapper.vm.reversedString).toBe('gnirtS')
    expect(wrapper.find('.text-green-500').text()).toContain('Reversed String: gnirtS')
  })

  it('should display error message when API call fails', async () => {
    vi.mocked(axios.post).mockRejectedValueOnce(new Error('Network Error'))
    await wrapper.vm.sendString()

    await wrapper.vm.$nextTick()
    expect(wrapper.vm.errorMessage).toBe('Could not connect to the server.')
    expect(wrapper.find('.text-red-500').text()).toContain(
      'Error: Could not connect to the server.'
    )
  })
})
