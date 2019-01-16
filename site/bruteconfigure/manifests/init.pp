class bruteconfigure {
	#copu foremanbrute
	file { '/usr/local/bin/foremanBrute':
		ensure => 'present',
		mode => '0744',
		source => 'puppet:///modules/bruteconfigure/foremanBrute.py',
	}
	#make it executable

	#install requirements
        package { 'python-pip':
  		ensure   => latest,
	}
	package {['requests', 'beautifulsoup']:
  		ensure  => installed,
		provider => 'pip',
	}
	#package (['requests', 'argparse', 'urllib', 're', 'beautifulsoup4'], {
        # ensure   => present,
        # provider => 'pip',
        # #require  => [ Package['python-pip'], ],
        #})


}
