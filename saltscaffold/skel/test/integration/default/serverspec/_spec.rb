require 'serverspec'

# Required by serverspec
set :backend, :exec


describe package('screen') do
  it { should be_installed }
end

describe file('/tmp/config.conf'), :if => os[:family] == 'debian' do
    it { should be_file }
    it { should be_mode 600 }
    it { should be_owned_by 'root' }
    it { should be_grouped_into 'root' }
    its(:content) { should match /test string please ignore/ }
end
