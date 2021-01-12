{{ with secret "pki/internal/issue/consul" "common_name=consul.service.consul" }}
{{- .Data.private_key }}{{ end }}
